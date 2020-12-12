from waitress import serve
import appweb

serve(appweb.app, host='0.0.0.0', port=8080)
