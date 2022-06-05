window.addEventListener("load" , function (){

    //.message_closeがクリックされた時、その親要素のmessage_areaを非表示にする
    $(".message_close").on("click", function(){ $(this).parents(".message_area").css({"display":"none"}); });



    //マップの表示位置を指定(緯度・経度)
    MAP     = L.map('map').setView([34.6217684, -227.2109985], 9);
    MARKER  = null;

    //地図データはOSMから読み込み
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(MAP);


    //予め用意した定数のPLACESから1つずつ取り出して、マーカーを配置する。
    for (let place of PLACES ){
        L.marker([place["lat"], place["lon"]]).addTo(MAP).bindPopup(place["comment"]).openPopup();
    }



    //MAP.on('click', function(e){ map_click(e); });
    MAP.on('click', map_click );

    /*
    $("#set_gps").on("click", function(){
        console.log("ゲットロケーション");
        get_location();
    });
    */
    $("#set_gps").on("click", get_location );

});

//マウスクリックで緯度と経度の取得とポイント設置
function map_click(e) {

    console.log(e.latlng["lat"]);
    console.log(e.latlng["lng"]);

    set_marker(e.latlng["lat"],e.latlng["lng"]);
}
function set_marker(lat,lon){

    if (MARKER){
        MAP.removeLayer(MARKER);
    }

    MARKER  = L.marker([lat, lon]).addTo(MAP);

    $("#lat_input").val(Math.round(lat*1000000)/1000000);
    $("#lon_input").val(Math.round(lon*1000000)/1000000);
}
function get_location(){

    // ブラウザが geolocation に対応しているか否かを確認
    if("geolocation" in navigator){

        //ここでGPSにアクセスしている(取得までにタイムラグがある。)
        let option = {
            "enableHighAccuracy": true,
            "timeout": 10000,
            "maximumAge": 0,
        };
        navigator.geolocation.getCurrentPosition(set_location, show_error, option);
    }else{
        alert("ブラウザが位置情報取得に対応していません");
    }

    function set_location(pos){
        // 緯度・経度を取得
        let lat = pos.coords.latitude;
        let lon = pos.coords.longitude;

        console.log(lat);
        console.log(lon);

        //この経度、360度でマイナスする。
        set_marker(lat,lon-360);
    }

    // エラー時に呼び出される関数
    function show_error(err){
        switch(err.code){
            case 1 : alert("位置情報の利用が許可されていません"); break;
            case 2 : alert("デバイスの位置が判定できません"); break;
            case 3 : alert("タイムアウトしました"); break;
            default : alert(err.message);
        }
    }


}
