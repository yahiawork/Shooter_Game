# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['--add-file=C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20260331.160100.0\\data\\student\\5332248\\188171\\galaxy.jpg;asteroid.png', '--add-file=C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20260331.160100.0\\data\\student\\5332248\\188171\\galaxy.jpg;rocket.png', '--add-file=C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20260331.160100.0\\data\\student\\5332248\\188171\\galaxy.jpg;ufo.png', '--add-file=C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20260331.160100.0\\data\\student\\5332248\\188171\\galaxy.jpg;galaxy.png', '--add-file=C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20260331.160100.0\\data\\student\\5332248\\188171\\galaxy.jpg;bullet.png', '--add-file=C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20260331.160100.0\\data\\student\\5332248\\188171\\galaxy.jpg;space.ogg', '--add-file=C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20260331.160100.0\\data\\student\\5332248\\188171\\galaxy.jpg;backrooms.ogg', '--add-file=C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20260331.160100.0\\data\\student\\5332248\\188171\\galaxy.jpg;fire.ogg', 'shooter_game.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='galaxy.jpg;asteroid',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['asteroid.png'],
)
