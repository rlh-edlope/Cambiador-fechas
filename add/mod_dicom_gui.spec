# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['mod_dicom_gui.py'],
    pathex=['/home/rlh/Escritorio/Dist/Cambiador de fechas/V2.0 Linux'],
    binaries=[],
    datas=[
        ('CFI_512.png','.'),
        ('CFI_256.png','.'),
        ('CFI_128.png','.'),
        ('CFI_96.png','.'),
        ('CFI_72.png','.'),
        ('CFI_64.png','.'),
        ('CFI_48.png','.'),
        ('CFI_32.png','.'),
        ('CFI_24.png','.'),
        ('CFI_16.png','.'),
        ('CFI.ico','.')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Cambiador Fechas',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
