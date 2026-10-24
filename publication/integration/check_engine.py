"""Consumer integration: fixed visuals and all historical product adapters.

Read-only; no C++ execution, PDF compilation, historical record mutation or publication.
"""
import argparse
import ast
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
BASE='7fb0ad0c85a4835fabe6482a9e73828d81f25b6a'


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--engine',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    sys.path.insert(0,str(args.engine/'engine'))
    import fidelity, preview, pub, source_model, project
    selected=project.load(args.engine.resolve(),ROOT/'publication/standalone.json','cpp-handbook',pub)
    project.engine_snapshot(selected,pub)
    unchanged=[]
    for name in ('latex/kb-base.sty','latex/kbbook.cls','engine/filters/blocks.lua','engine/preview_audit.py','engine/links.py'):
        before=subprocess.check_output(['git','--no-replace-objects','show',BASE+':publication/'+name],cwd=ROOT)
        if (args.engine/name).read_bytes()!=before:raise RuntimeError('frozen visual changed: '+name)
        unchanged.append(name)
    def functions(raw):
        return {n.name:ast.dump(n,include_attributes=False) for n in ast.parse(raw).body
                if isinstance(n,ast.FunctionDef) and n.name in ('tables_to_records','bind_code_roles','code_labels','compose','build_view')}
    before=subprocess.check_output(['git','--no-replace-objects','show',BASE+':publication/engine/preview.py'],cwd=ROOT)
    if functions(before)!=functions((args.engine/'engine/preview.py').read_bytes()):raise RuntimeError('visual function changed')
    reports=[]
    for path in sorted((ROOT/'publication/profiles').glob('*/profile.json')):
        config=json.loads(path.read_text())
        spec=importlib.util.spec_from_file_location('product_adapter',path.with_name('adapter.py'))
        adapter=importlib.util.module_from_spec(spec);spec.loader.exec_module(adapter)
        for src in config['sources']:
            raw=(ROOT/src['path']).read_bytes() if src['revision']=='WORKTREE' else source_model.blob(ROOT,src['revision'],src['path'],pub)
            parsed=json.loads(subprocess.check_output(['pandoc','-f',config.get('source_format','markdown-smart'),'-t','json'],input=raw))
            audit=fidelity.adapt_checked(parsed,adapter,src,preview.text)[-1]
            reports.append({'profile':config['id'],'source':src['id'],'source_sha256':hashlib.sha256(raw).hexdigest(),
                            'revision':src['revision'],'status':audit['status']})
    report={'status':'PASS','engine_pin':selected.config['engine'],'unchanged_files':unchanged,
            'unchanged_visual_functions':sorted(functions(before)), 'source_adapter_checks':reports,
            'boundary':'Local consumer checks; not PDF, C++ or whole-book technical qualification'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as output:json.dump(report,output,ensure_ascii=False,indent=2);output.write('\n')
    print(json.dumps({'status':'PASS','source_adapter_checks':len(reports)}))


if __name__=='__main__':main()
