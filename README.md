# testsocket
 Python Binance Socket Test
 
 Create  config.py
  API_KEY = 'put your binance key here'
  API_SECRET ='put your binance secret here'

**web-socket-streams.md**
	https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md
	wss://stream.binance.com:9443
	
	Command:	npm install -g wscat
	Command:	wscat -c wss://stream.binance.com:9443/ws/btcusdt@trade
	Command:	wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m
	Command:	wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m | tee dataset.txt

**Connect to WebSocket using JavaScript**	
	https://developer.mozilla.org/en-US/docs/Web/API/WebSocket
	https://developer.mozilla.org/en-US/docs/Web/API/WebSocket#examples
			// Create WebSocket connection.
			const socket = new WebSocket('wss://stream.binance.com:9443/ws/btcusdt@trade');

			// Connection opened
			socket.addEventListener('open', function (event) {
				socket.send('Connected to the server');
			});

			// Listen for messages
			socket.addEventListener('message', function (event) {
				console.log('Message from server ', event.data);
			});	

Introduce Charts on top of the WebSockets			
	https://www.tradingview.com/lightweight-charts/
	CDN: https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js
	
	
**Introduce Python TA lib**
	Latest Python Installation 	https://www.python.org/downloads/
	
	PIP Install
		https://datatofish.com/add-python-to-windows-path/
		
		Binance Endpoints https://python-binance.readthedocs.io/en/latest/
			--the below should be ran under Administrator rights (run 'pip install python-binance' under Anmin rights on Windows)
			PIP Install 				https://pypi.org/project/pip/
			Command: 					py -m pip install -U pip
	Command: python getdata.py

	https://binance-docs.github.io/apidocs/futures/en/#compressed-aggregate-trades-list
	CSV https://docs.python.org/3/library/csv.html
	CSV historical https://python-binance.readthedocs.io/en/latest/market_data.html#id3

**TA lib**
	https://ta-lib.org/
	https://ta-lib.org/function.html
	
	https://github.com/mrjbq7/ta-lib
	Command: pip install TA-Lib
		error: Microsoft Visual C++ 14.0 is required. Get it with "Build Tools for Visual Studio"
		pip install --upgrade setuptools
		https://docs.microsoft.com/ru-ru/visualstudio/install/install-visual-studio?view=vs-2019&viewFallbackFrom=vs-2019%2F#_step-4---choose-workloads
	    error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
	TALIB manual install https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
	Download TA_Lib-0.4.19-cp39-cp39-win_amd64.whl
	Command: pip install .\TA_Lib-0.4.19-cp39-cp39-win_amd64.whl
	SOLVED!!!

**Numpy and CSV	**
	https://stackoverflow.com/questions/25614749/how-to-import-csv-file-as-numpy-array-in-python
	
