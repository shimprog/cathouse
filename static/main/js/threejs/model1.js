window.onload =function (){
    var width = window.innerWidth;
    var height = window.innerHeight;
    var canvas = document.getElementById('canvas');

    canvas.setAttribute('width', width);
    canvas.setAttribute('height', height);

    var renderer = new THREE.WebGLRenderer({canvas: canvas});
    renderer.setClearColor(0x000000);

    renderer.setSize( window.innerWidth, window.innerHeight );
    document.body.appendChild( renderer.domElement );

    var scene = new THREE.Scene();
    scene.background = new THREE.Color( 0xcccccc );

    var camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 5000);
    camera.position.set(0, 0, 1000);

    var controls = new OrbitControls( camera, renderer.domElement );
    //controls.update() must be called after any manual changes to the camera's transform
    camera.position.set( 0, 20, 100 );
    controls.update();

    var loader = new GLTFLoader();
    loader.load('{% static 'main/houses/house1.gltf' %}', function (gltf){

        scene.add(gltf.scene);

    });

    var light = new THREE.AmbientLight(0xffffff);
    scene.add(light);

    var geometry = new THREE.SphereGeometry(200, 12, 12);
    var material = new THREE.MeshBasicMaterial({color: 0x00ff00, wireframe: true});
    var mesh = new THREE.Mesh(geometry,material);
    scene.add(mesh);

    renderer.render(scene, camera);

    function animate() {

        requestAnimationFrame(animate);

        // required if controls.enableDamping or controls.autoRotate are set to true
        controls.update();

        renderer.render(scene, camera);
    }
    animate()
}
