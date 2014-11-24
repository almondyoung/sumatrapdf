{
    'includes': [
        'zlib.gyp',
        '../ext/libjpeg-turbo/libjpeg.gyp',
        'jbig2dec.gyp',
        'freetype.gyp',
        'openjpeg.gyp',
    ],
    'targets': [
        {
            'target_name': 'mupdf',
            'type': 'static_library',
            'dependencies': [
                'zlib',
                'libjpeg',
                'jbig2dec',
                'freetype',
                'openjpeg',
            ],
            'defines': [
                'NOCJKFONT',
                'NODROIDFONT',
                'SHARE_JPEG',
            ],
            'include_dirs': [
                "../mupdf/include",
                "../mupdf/generated",
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                    "../mupdf/include",
                ],
            },
            'msvs_disabled_warnings': [4996],
            'conditions': [
                [ 'OS=="win"', {
                  'variables': {
                    'nasm_path': '<(nasm_dir)/nasm<(EXECUTABLE_SUFFIX)',
                    'conditions': [
                      [ 'target_arch=="ia32"', {
                        'nasm_flags': [
                          '-f', 'win32',
                        ],
                      }, {
                        'nasm_flags': [
                          '-f', 'win64',
                        ],
                      }],
                    ],
                  },
                }],
            ],
            'rules': [
            {
              'rule_name': 'assemble',
              'extension': 'asm',
              'conditions': [
                [ 'target_arch!="arm"', {
                  'inputs': [ '<(nasm_path)', ],
                  'outputs': [
                    '<(shared_generated_dir)/<(RULE_INPUT_ROOT).<(object_suffix)',
                  ],
                  'action': [
                    '<(nasm_path)',
                    '<@(nasm_flags)',
                    '-I', "mupdf///",
                    '-o', '<(shared_generated_dir)/<(RULE_INPUT_ROOT).<(object_suffix)',
                    '<(RULE_INPUT_PATH)',
                  ],
                  'process_outputs_as_sources': 1,
                  'message': 'Building <(RULE_INPUT_ROOT).<(object_suffix)',
                }],
              ]
            },
            ],
            'sources': [
                "../mupdf/source/fitz/bbox-device.c",
                "../mupdf/source/fitz/bitmap.c",
                "../mupdf/source/fitz/buffer.c",
                "../mupdf/source/fitz/colorspace.c",
                "../mupdf/source/fitz/compressed-buffer.c",
                "../mupdf/source/fitz/context.c",
                "../mupdf/source/fitz/crypt-aes.c",
                "../mupdf/source/fitz/crypt-arc4.c",
                "../mupdf/source/fitz/crypt-md5.c",
                "../mupdf/source/fitz/crypt-sha2.c",
                "../mupdf/source/fitz/device.c",
                "../mupdf/source/fitz/document.c",
                "../mupdf/source/fitz/draw-affine.c",
                "../mupdf/source/fitz/draw-blend.c",
                "../mupdf/source/fitz/draw-device.c",
                "../mupdf/source/fitz/draw-edge.c",
                "../mupdf/source/fitz/draw-glyph.c",
                "../mupdf/source/fitz/draw-imp.h",
                "../mupdf/source/fitz/draw-mesh.c",
                "../mupdf/source/fitz/draw-paint.c",
                "../mupdf/source/fitz/draw-path.c",
                "../mupdf/source/fitz/draw-scale-simple.c",
                "../mupdf/source/fitz/draw-unpack.c",
                "../mupdf/source/fitz/error.c",
                "../mupdf/source/fitz/filter-basic.c",
                "../mupdf/source/fitz/filter-dct.c",
                "../mupdf/source/fitz/filter-fax.c",
                "../mupdf/source/fitz/filter-flate.c",
                "../mupdf/source/fitz/filter-jbig2.c",
                "../mupdf/source/fitz/filter-leech.c",
                "../mupdf/source/fitz/filter-lzw.c",
                "../mupdf/source/fitz/filter-predict.c",
                "../mupdf/source/fitz/font.c",
                "../mupdf/source/fitz/ftoa.c",
                "../mupdf/source/fitz/function.c",
                "../mupdf/source/fitz/gdiplus-device.cpp",
                "../mupdf/source/fitz/geometry.c",
                "../mupdf/source/fitz/getopt.c",
                "../mupdf/source/fitz/glyph.c",
                "../mupdf/source/fitz/halftone.c",
                "../mupdf/source/fitz/hash.c",
                "../mupdf/source/fitz/image.c",
                "../mupdf/source/fitz/link.c",
                "../mupdf/source/fitz/list-device.c",
                "../mupdf/source/fitz/load-jpeg.c",
                "../mupdf/source/fitz/load-jpx.c",
                "../mupdf/source/fitz/load-jxr.c",
                "../mupdf/source/fitz/load-png.c",
                "../mupdf/source/fitz/load-tiff.c",
                "../mupdf/source/fitz/memory.c",
                "../mupdf/source/fitz/outline.c",
                #"../mupdf/source/fitz/output-pcl.c",
                #"../mupdf/source/fitz/output-pwg.c",
                "../mupdf/source/fitz/output.c",
                "../mupdf/source/fitz/path.c",
                "../mupdf/source/fitz/pixmap.c",
                "../mupdf/source/fitz/printf.c",
                "../mupdf/source/fitz/shade.c",
                "../mupdf/source/fitz/stext-device.c",
                "../mupdf/source/fitz/stext-output.c",
                "../mupdf/source/fitz/stext-paragraph.c",
                "../mupdf/source/fitz/stext-search.c",
                "../mupdf/source/fitz/store.c",
                "../mupdf/source/fitz/stream-open.c",
                #"../mupdf/source/fitz/stream-prog.c",
                "../mupdf/source/fitz/stream-read.c",
                "../mupdf/source/fitz/string.c",
                "../mupdf/source/fitz/strtod.c",
                #"../mupdf/source/fitz/svg-device.c",
                #"../mupdf/source/fitz/test-device.c",
                "../mupdf/source/fitz/text.c",
                "../mupdf/source/fitz/time.c",
                "../mupdf/source/fitz/trace-device.c",
                "../mupdf/source/fitz/transition.c",
                "../mupdf/source/fitz/tree.c",
                "../mupdf/source/fitz/ucdn.c",
                "../mupdf/source/fitz/ucdn.h",
                "../mupdf/source/fitz/unicodedata_db.h",
                "../mupdf/source/fitz/xml.c",
                "../mupdf/source/pdf/pdf-annot-edit.c",
                "../mupdf/source/pdf/pdf-annot.c",
                "../mupdf/source/pdf/pdf-appearance.c",
                "../mupdf/source/pdf/pdf-clean.c",
                "../mupdf/source/pdf/pdf-cmap-load.c",
                "../mupdf/source/pdf/pdf-cmap-parse.c",
                "../mupdf/source/pdf/pdf-cmap-table.c",
                "../mupdf/source/pdf/pdf-cmap.c",
                "../mupdf/source/pdf/pdf-colorspace.c",
                "../mupdf/source/pdf/pdf-crypt.c",
                "../mupdf/source/pdf/pdf-device.c",
                "../mupdf/source/pdf/pdf-encoding.c",
                "../mupdf/source/pdf/pdf-encodings.h",
                "../mupdf/source/pdf/pdf-event.c",
                "../mupdf/source/pdf/pdf-field.c",
                "../mupdf/source/pdf/pdf-font.c",
                "../mupdf/source/pdf/pdf-fontfile.c",
                "../mupdf/source/pdf/pdf-form.c",
                "../mupdf/source/pdf/pdf-ft-tools.c",
                "../mupdf/source/pdf/pdf-function.c",
                "../mupdf/source/pdf/pdf-glyphlist.h",
                "../mupdf/source/pdf/pdf-image.c",
                "../mupdf/source/pdf/pdf-interpret-imp.h",
                "../mupdf/source/pdf/pdf-interpret.c",
                "../mupdf/source/pdf/pdf-lex.c",
                "../mupdf/source/pdf/pdf-metrics.c",
                "../mupdf/source/pdf/pdf-nametree.c",
                "../mupdf/source/pdf/pdf-object.c",
                "../mupdf/source/pdf/pdf-op-buffer.c",
                "../mupdf/source/pdf/pdf-op-filter.c",
                "../mupdf/source/pdf/pdf-op-run.c",
                "../mupdf/source/pdf/pdf-outline.c",
                "../mupdf/source/pdf/pdf-page.c",
                "../mupdf/source/pdf/pdf-parse.c",
                "../mupdf/source/pdf/pdf-pattern.c",
                "../mupdf/source/pdf/pdf-pkcs7.c",
                "../mupdf/source/pdf/pdf-repair.c",
                "../mupdf/source/pdf/pdf-run.c",
                "../mupdf/source/pdf/pdf-shade.c",
                "../mupdf/source/pdf/pdf-store.c",
                "../mupdf/source/pdf/pdf-stream.c",
                "../mupdf/source/pdf/pdf-type3.c",
                "../mupdf/source/pdf/pdf-unicode.c",
                "../mupdf/source/pdf/pdf-write.c",
                "../mupdf/source/pdf/pdf-xobject.c",
                "../mupdf/source/pdf/pdf-xref-aux.c",
                "../mupdf/source/pdf/pdf-xref.c",
                "../mupdf/source/xps/xps-common.c",
                "../mupdf/source/xps/xps-doc.c",
                "../mupdf/source/xps/xps-glyphs.c",
                "../mupdf/source/xps/xps-gradient.c",
                "../mupdf/source/xps/xps-image.c",
                "../mupdf/source/xps/xps-outline.c",
                "../mupdf/source/xps/xps-path.c",
                "../mupdf/source/xps/xps-resource.c",
                "../mupdf/source/xps/xps-tile.c",
                "../mupdf/source/xps/xps-util.c",
                "../mupdf/source/xps/xps-zip.c",
                "../mupdf/include/mupdf/cbz.h",
                "../mupdf/include/mupdf/fitz.h",
                "../mupdf/include/mupdf/img.h",
                "../mupdf/include/mupdf/pdf-tools.h",
                "../mupdf/include/mupdf/pdf.h",
                "../mupdf/include/mupdf/tiff.h",
                "../mupdf/include/mupdf/xps.h",
                "../mupdf/font_base14.asm",
            ],
        }
    ],
}
