function fetchData() {
    fetch('http://localhost:63342/ChemEditorProject/client/index.html?_ijt=v4p31a2hbbfdj06fmks0j4e9g2&_ij_reload=RELOAD_ON_SAVE').then(response =>{
        const data = response.json();
    });

}

    fetchData();





















