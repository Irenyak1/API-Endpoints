from flask import Flask, jsonify, request, make_response
from api import app
from .models import User, users, Request, requests



@app.route('/api/v1/users/requests', methods=['POST'])
def create_request():
    # getting user request data
    user_request_data = request.get_json()

    if not user_request_data:
        return jsonify({'message': 'Please fill all the fields'}), 400
        
    clientname = str(user_request_data.get('clientname')).strip()
    clientcontact = str(user_request_data.get('clientcontact')).strip()
    clientemail = str(user_request_data.get('clientemail')).strip()
    locationaddress = str(user_request_data.get('locationaddress')).strip()
    department = user_request_data.get('department').strip()
    dateneeded = user_request_data.get('dateneeded').strip()
    workassignedto = user_request_data.get('workassignedto').strip()
    workbilledto = user_request_data.get('workbilledto').strip()
    detailsofrequest = user_request_data.get('detailsofrequest').strip()
    

    # validate user request data
    if not clientname:
        return jsonify({'message': 'Name is required'}), 400

    if not clientcontact:
        return jsonify({'message': 'Contact is required'}), 400

    if not clientemail:
        return jsonify({'message': 'Email is required'}), 400

    if not locationaddress:
        return jsonify({'message': 'Location address is required'}), 400

    if not department:
        return jsonify({'message': 'department is required'}), 400

    if not dateneeded:
        return jsonify({'message': 'dateneeded is required'}), 400

    if not workassignedto:
        return jsonify({'message': 'workassignedto is required'}), 400

    if not workbilledto:
        return jsonify({'message': 'workbilledto is required'}), 400

    if not detailsofrequest:
        return jsonify({'message': 'detailsofrequest is required'}), 400

    user_request_data['id'] = len(requests)
    # store your user request data to your database
    requests.append(user_request_data)

    return jsonify({'message': f'Request from {clientname} has been successfully submitted'}), 201


@app.route('/api/v1/users/requests', methods=['GET'])
def get_all_requests():
    return jsonify({'requests': requests}), 200


#@app.route('/api/v1/users/requests/<int:request_id>', methods=['GET'])
#def get_request(request_id):
#    for each_request in requests:
#        if each_request.get('request_id') == request_id:
#            return jsonify({'request': each_request})
#    return jsonify({'error': 'Request Not Found'}), 404
@app.route('/api/v1/users/requests/<int:request_id>', methods=['GET'])
def get_a_request(request_id):
    """ Endpoint to fetch a request """
    if len(requests) < 1:
        return jsonify({"status":"Failure",
        "Oops!":"There are no requests"
        }),404
    for user_request in requests:
        if user_request.request_id ==request_id:
            return jsonify({'Request': user_request.__dict__}),200
    
    return jsonify({'error':'User Not Found'}), 404


@app.route("/api/v1/users/requests/<int:request_id>", methods=['PUT'])
def update_request(request_id):
    """ Endpoint to modify a given request"""
    if len(requests) < 1:
        return jsonify({
            "status":"Failure",
            "Oops":"There is no request to modify"}), 404
    
    if len(requests) >= 1:
        request_data = request.get_json()
        clientname =  request_data.get("clientname")
        clientcontact = request_data.get("clientcontact")
        clientemail =  request_data.get("clientemail")
        locationaddress = request_data.get("locationaddress")
        department = request_data.get("department")
        dateneeded  = request_data.get("dateneeded")
        workassignedto = request_data.get("workassignedto")
        workbilledto = request_data.get("workbilledto")
        detailsofrequest = request_data.get("detailsofrequest")

        for user_request in requests:
            if user_request.request_id == int(request_id):
                user_request.clientname = clientname
                user_request.clientcontact = clientcontact
                user_request.clientemail = clientemail
                user_request.locationaddress= locationaddress
                user_request.department = department
                user_request.dateneeded = dateneeded
                user_request.workassignedto = workassignedto
                user_request.workbilledto = workbilledto
                user_request.detailsofrequest = detailsofrequest

            return jsonify({
                "request":user_request.__dict__,
                "status":"OK",
                "Great":"user request has been successfully updated",
            })

