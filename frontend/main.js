if (window.File && window.FileReader && window.FileList && window.Blob) {
  // Great success! All the File APIs are supported.
  const uploadbtm = document.getElementById('uploadbtn')
  const fileSelector = document.getElementById('file-selector');
  let file = "";

  uploadbtm.addEventListener('click', (e)=>{
    e.preventDefault()
    if(file != "" && file){
      var formData = new FormData();  
      // HTML file input, chosen by user
      formData.append("file", file);


      fetch("http://127.0.0.1:5000/api/upload", {
              body: formData,
              method: "post"
      })
      .then(response => response.json())
      .then(() => alert('data saved sucessfully'))
      .catch(err=>{
        console.log(err)
      })
  

    }else{
      alert('No file selected.')
    }

  })

  fileSelector.addEventListener('change', (event) => {
    file= event.target.files[0];
    event.preventDefault()
    console.log(file);
  });


} else {
  alert('The File APIs are not fully supported in this browser.');
}

  
