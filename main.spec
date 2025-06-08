# -*- mode: python ; coding: utf-8 -*-


import os
from PyInstaller.utils.hooks import collect_data_files

# Collect SVG icons and other resources
# For PyQt6, just collect SVGs from the icons directory

datas = [
    ('src/icons/' + f, 'icons')
    for f in os.listdir('src/icons') if f.endswith('.svg')
]

block_cipher = None

a = Analysis(
    ['src/main.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'PyQt6',
        'PyQt6.QtCore',
        'PyQt6.QtGui',
        'PyQt6.QtWidgets',
        'PyQt6.QtSvg',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[
        'gi',
        'gi.repository.Gtk',
        'gi.repository.Gio',
        'gi.repository.Gdk',
        'gi.repository.GLib',
        'gi.repository.GdkPixbuf',
        'gi.repository.Pango',
        'gi.repository.Rsvg'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='intertech',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False  # Set to True if you want console output
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='intercalc'
)
