# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('VERSION', '.'),
        ('README.md', '.')
    ],
    hiddenimports=['yaml', 'psutil'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['pytest', 'black', 'flake8'], # Drops development weight completely
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
    name='NitroCoreOptimizer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True, # Compresses binary footprint automatically
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False, # Set to False to hide the ugly background black CMD prompt box
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements=file,
    uac_admin=True, # Crucial: Forces the compiled executable to request Admin privileges right at launch!
)
