from flask import Blueprint, jsonify, request
from src.main.models.seguridad.acciones_usuario.AccionesUsuarioDao import AccionesUsuarioDao

# Modularizar
aur = Blueprint("accionesUsuarioMod", __name__)
aud = AccionesUsuarioDao()

@aur.route("/get_acciones")
def getAcciones():
    items = aud.listarTodos()
    lista_final = []
    if len(items)<1:
        return jsonify("{{'estado':'error', 'mensaje':'No ha elementos}"),200
    for item in items:
        lista_final.append({
            "id": item.id, "accion": item.accion, "descripcion": item.descripcion
        })
    return jsonify(lista_final), 200

@aur.route("/get_acciones_by_id/<id>")
def getAccionById(id):
    item = aud.getById(id)
    return jsonify(dict(id=item.id, accion=item.accion, descripcion=item.descripcion)), 200

@aur.route("/add_accion", methods=["POST"])
def addAccion():
    json = request.get_json()
    resp = aud.agregar(json['accion'], json['descripcion'])
    if resp==True:
        return jsonify("{'estado':'correcto', 'mensaje':'Se ha agregado'}"), 201
    return jsonify("{'estado':'error', 'mensaje':'No se ha agregado'}"), 500

@aur.route("/modify_accion_by_id", methods=["PUT"])
def modifyAccionById():
    json = request.get_json()
    transaction_key = ['id', 'accion']
    if not all(key in json for key in transaction_key):
        return 'Faltan algunos elementos de la transacción', 400
    resp = aud.modificarAccion(json['id'], json['accion'])
    if resp==True:
        return jsonify("{'estado':'correcto', 'mensaje':'Se ha modificado'}"), 200
    return jsonify("{'estado':'error', 'mensaje':'No se ha modificado'}")

@aur.route("/modify_accion_descripcion_by_id", methods=["PUT"])
def modifyAccionDescripcionById():
    json = request.get_json()
    transaction_key = ['id', 'descripcion']
    if not all(key in json for key in transaction_key):
        return 'Faltan algunos elementos de la transacción', 400
    resp = aud.modificarDescripcion(json['id'], json['descripcion'])
    if resp==True:
        return jsonify("{'estado':'correcto', 'mensaje':'Se ha modificado'}"), 200
    return jsonify("{'estado':'error', 'mensaje':'No se ha modificado'}")

@aur.route("/delete/<int:id>", methods=['DELETE'])
def deleteAccion(id):
    resp = aud.eliminar(id)
    if resp==True:
        return jsonify("{'estado':'correcto', 'mensaje':'Se ha eliminado'}"), 200
    return jsonify("{'estado':'error', 'mensaje':'No se ha eliminado'}")