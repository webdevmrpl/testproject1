const domain = 'http://localhost:8000/';

window.onload = function (){
    const list = document.getElementById('list');
    const rubricListLoader = new XMLHttpRequest();
    rubricListLoader.onreadystatechange = function (){
        if(rubricListLoader.readyState == 4){
            if(rubricListLoader.status == 200){
                const data = JSON.parse(rubricListLoader.responseText);
                let s = '<ul>';
                for (let i=0; i< data.length;i++){
                    s+= '<li>' + data[i].name + '</li>'
                }
                s+= '<ul>'
                list.innerHTML =s;
            }
        }
    }

function rubricListLoad(){
    rubricListLoader.open('GET',domain + 'api/rubrics', true)
    rubricListLoader.send()
}
rubricListLoad();

}