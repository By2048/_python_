import shutil

shutil.get_archive_formats()
shutil.make_archive('/tmp/f1', 'zip', root_dir='/tmp/f1/')

shutil.move('/tmp/f1', '/tmp/f2')
shutil.copytree('/tmp/f1/', '/tmp/f2/')
shutil.copytree('/tmp/f1/', '/tmp/f2/', ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))
shutil.rmtree('/tmp/f1/')
shutil.copy('/tmp/f1', '/tmp/f2')
shutil.copyfile('/tmp/f1', '/tmp/f2')
shutil.copymode('/tmp/f1', '/tmp/f2')
shutil.copystat('/tmp/f1', '/tmp/f2')
shutil.copy2('/tmp/f1', '/tmp/f2')
