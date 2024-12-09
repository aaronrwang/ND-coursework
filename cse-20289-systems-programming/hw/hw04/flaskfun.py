from flask import Flask, request, send_file, abort
import os


app = Flask(__name__)
#activate with python3 flaskfun.py
#example test case 
#
#http://student11.cse.nd.edu:54003/hw04?prepend=RPI01&year=2024&month=03&interface=WiFi
#Put this in the google or safari search bar. Change the year, month, interface, and the prepend based on the file. 



PORT = 54003

@app.route('/hw04', methods=['GET'])
def hw04():
    year = request.args.get('year')
    month = request.args.get('month')
    interface = request.args.get('interface')
    prepend = request.args.get('prepend', '')
    
    if not year or not month or not interface:
        abort(400, description="Missing year, month, or interface parameters.")
        #checks to see if a parameter is missing


    pdf_filename = f'{prepend}-{year}-{month}-{interface}.pdf'
    #Looks for the correct arguements 

    if not os.path.exists(pdf_filename):
        abort(404, description="PDF not found.")
    
    return send_file(pdf_filename, as_attachment=True)
    
if __name__ == '__main__':
    app.run(host='student11.cse.nd.edu', port=PORT) #makes it run on the correct host
