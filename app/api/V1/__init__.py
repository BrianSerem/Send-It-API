"""Contain urls and blueprint."""
from flask import Blueprint
from flask_restful import Api
from .views.parcelviews import GetParcels, CreateParcel
from .views.parcelviews import CancelSpecificParcel, GetUserParcels
from .views.parcelviews import PendingParcels, DeliveredParcels
from .views.parcelviews import MovingParcels, SpecificParcel, DeliverParcel
from .views.parcelviews import DeclinedParcels, MarkParcelInTransit
from .views.parcelviews import ApproveParcel, GetAcceptedParcels, DeclineParcel


version_1 = Blueprint('v1', __name__)

api = Api(version_1, prefix="/api/v1")

api.add_resource(SpecificParcel, '/parcels/<int:id>')
api.add_resource(CreateParcel, '/parcels')
api.add_resource(GetParcels, '/parcels')

api.add_resource(GetAcceptedParcels, '/parcels/accepted')
api.add_resource(DeliveredParcels, '/parcels/delivered')
api.add_resource(DeclinedParcels, '/parcels/declined')
api.add_resource(MovingParcels, '/parcels/moving')
api.add_resource(PendingParcels, '/parcels/pending')

api.add_resource(DeliverParcel, '/parcels/<int:id>/delivered')
api.add_resource(ApproveParcel, '/parcels/<int:id>/approved')
api.add_resource(MarkParcelInTransit, '/parcels/<int:id>/moving')
api.add_resource(DeclineParcel, '/parcels/<int:id>/declined')
api.add_resource(CancelSpecificParcel, '/parcels/<int:id>/cancel')
api.add_resource(GetUserParcels, '/users/<int:user_id>/parcels')
