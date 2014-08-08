from scrapy.http import Request, FormRequest, HtmlResponse
import sys;
sys.path.append("/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/gtk-2.0/gtk/")

import gtk
import webkit
import jswebkit
import spider.settings as settings
 
class WebkitDownloader( object ):
    def process_request( self, request, spider ):
        if spider.name in settings.WEBKIT_DOWNLOADER:
                print 'hhhhhkkklsdfklsdjflksadjflkdsajfls'
            # if( type(request) is not FormRequest ):
                webview = webkit.WebView()
                webview.connect( 'load-finished', lambda v,f: gtk.main_quit() )
                webview.load_uri( request.url )
                gtk.main()
                gtk.main()
                gtk.main()
                gtk.main()
                # gtk.main()
                js = jswebkit.JSContext( webview.get_main_frame().get_global_context() )
                renderedBody = str( js.EvaluateScript( 'document.body.innerHTML' ) )

                return HtmlResponse( request.url, body=renderedBody )



