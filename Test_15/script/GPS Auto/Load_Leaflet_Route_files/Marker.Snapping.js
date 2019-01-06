L.Marker.include({
	/**
	 * Snap to function
	 *
	 * @param <LatLng> latlng - original position
	 *
	 * @return <LatLng> - new position
	 */
	snapTo: function (latlng) {
		//console.log("hi");
		console.log(L.LineUtil.snapToLayers(latlng, this._leaflet_id, this.options.snapping));
		return L.LineUtil.snapToLayers(latlng, this._leaflet_id, this.options.snapping);
	}
});
