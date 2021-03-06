#
# Copyright (c) 2015 peeracle contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

{
  'targets': [
    {
      'target_name': 'curl',
      'type': 'static_library',
      'include_dirs': [
        'config/<(OS)/<(target_arch)',
        'config/<(OS)/<(target_arch)/curl',
        'include/curl',
        'include',
        'lib'
      ],
      'direct_dependent_settings': {
        'defines': [
          'CURL_STATICLIB',
        ],
        'include_dirs': [
          'config/<(OS)/<(target_arch)/curl',
        ],
      },
      'dependencies': [
        '<(DEPTH)/third_party/zlib/zlib.gyp:zlib',
        '<(peeracle_webrtc_root)/third_party/boringssl/boringssl.gyp:boringssl'
      ],
      'defines': [
        'HTTP_ONLY',
        'USE_OPENSSL',
        'USE_SSLEAY',
        'USE_IPV6',
        'HAVE_BORINGSSL',
        'HAVE_CONFIG_H',
        'BUILDING_LIBCURL',
        'CURL_STATICLIB'
      ],
      'sources': [
        'lib/file.c',
        'lib/timeval.c',
        'lib/base64.c',
        'lib/hostip.c',
        'lib/progress.c',
        'lib/formdata.c',
        'lib/cookie.c',
        'lib/http.c',
        'lib/sendf.c',
        'lib/ftp.c',
        'lib/url.c',
        'lib/dict.c',
        'lib/if2ip.c',
        'lib/speedcheck.c',
        'lib/ldap.c',
        'lib/version.c',
        'lib/getenv.c',
        'lib/escape.c',
        'lib/mprintf.c',
        'lib/telnet.c',
        'lib/netrc.c',
        'lib/getinfo.c',
        'lib/transfer.c',
        'lib/strequal.c',
        'lib/easy.c',
        'lib/security.c',
        'lib/curl_fnmatch.c',
        'lib/fileinfo.c',
        'lib/ftplistparser.c',
        'lib/wildcard.c',
        'lib/krb5.c',
        'lib/memdebug.c',
        'lib/http_chunks.c',
        'lib/strtok.c',
        'lib/connect.c',
        'lib/llist.c',
        'lib/hash.c',
        'lib/multi.c',
        'lib/content_encoding.c',
        'lib/share.c',
        'lib/http_digest.c',
        'lib/md4.c',
        'lib/md5.c',
        'lib/http_negotiate.c',
        'lib/inet_pton.c',
        'lib/strtoofft.c',
        'lib/strerror.c',
        'lib/amigaos.c',
        'lib/hostasyn.c',
        'lib/hostip4.c',
        'lib/hostip6.c',
        'lib/hostsyn.c',
        'lib/inet_ntop.c',
        'lib/parsedate.c',
        'lib/select.c',
        'lib/tftp.c',
        'lib/splay.c',
        'lib/strdup.c',
        'lib/socks.c',
        'lib/ssh.c',
        'lib/rawstr.c',
        'lib/curl_addrinfo.c',
        'lib/socks_gssapi.c',
        'lib/socks_sspi.c',
        'lib/curl_sspi.c',
        'lib/slist.c',
        'lib/nonblock.c',
        'lib/curl_memrchr.c',
        'lib/imap.c',
        'lib/pop3.c',
        'lib/smtp.c',
        'lib/pingpong.c',
        'lib/rtsp.c',
        'lib/curl_threads.c',
        'lib/warnless.c',
        'lib/hmac.c',
        'lib/curl_rtmp.c',
        'lib/openldap.c',
        'lib/curl_gethostname.c',
        'lib/gopher.c',
        'lib/idn_win32.c',
        'lib/http_negotiate_sspi.c',
        'lib/http_proxy.c',
        'lib/non-ascii.c',
        'lib/asyn-ares.c',
        'lib/asyn-thread.c',
        'lib/curl_gssapi.c',
        'lib/curl_ntlm.c',
        'lib/curl_ntlm_wb.c',
        'lib/curl_ntlm_core.c',
        'lib/curl_ntlm_msgs.c',
        'lib/curl_sasl.c',
        'lib/curl_multibyte.c',
        'lib/hostcheck.c',
        'lib/bundles.c',
        'lib/conncache.c',
        'lib/pipeline.c',
        'lib/dotdot.c',
        'lib/x509asn1.c',
        'lib/http2.c',
        'lib/curl_sasl_sspi.c',
        'lib/smb.c',
        'lib/curl_sasl_gssapi.c',
        'lib/curl_endian.c',
        'lib/curl_des.c',
        'lib/vtls/openssl.c',
        'lib/vtls/gtls.c',
        'lib/vtls/vtls.c',
        'lib/vtls/nss.c',
        'lib/vtls/polarssl.c',
        'lib/vtls/polarssl_threadlock.c',
        'lib/vtls/axtls.c',
        'lib/vtls/cyassl.c',
        'lib/vtls/schannel.c',
        'lib/vtls/darwinssl.c',
        'lib/vtls/gskit.c'
      ],
      'conditions': [
        ['OS == "linux"', {
          'link_settings': {
            'libraries': [
              '-lidn'
            ],
          },
        }],
        ['OS == "win"', {
          'msvs_settings': {
            'VCCLCompilerTool': {
              'CompileAs': '1',
              'WarningLevel': '3',
            }
          },
          'direct_dependent_settings': {
            'link_settings': {
              'libraries': [
                '-lws2_32.lib',
              ],
            },
          },
        }],
      ],
    }
  ]
}
