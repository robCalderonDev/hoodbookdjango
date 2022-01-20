$("#form_registro").validate({
    rules:{
        nombre:{
            required:true,
            minlength:3,
            maxlength:30,
        },
        apellidos:{
            required:true,
            minlength:3,
            maxlength:40,
        
        },
        email1:{
            required:true,
            
        },
        password:{
            required:true,
            minlength:6
        },
        password2:{
            required:true,
            equalTo:"#password"
        },
        terminos:{
            required:true
        }
    },
    messages:{
        nombre:{
            minlength:"Ingrese un nombre valido ",
            required:"Ingrese un nombre"
        },
        apellidos:{
            required:"Ingrese sus apellidos",
            minlength:"Ingrese apellidos correctos"
        },
        email1:{
            required:"Ingrese su email",
            email:"Formato de email incorrecto"
        },
        password:{
            required:"Ingrese una contraseña",
            minlength:"Su contraseña es muy corta"

        },
        password2:{
            required:"Ingrese de nuevo su contraseña",
            equalTo:"Contraseña incorrecta"
        },
        terminos:{
            required:"Acepte los terminos y condiciones",
        }
    }

})

$("#registrar").click(function(){
    if($("#form_registro").valid()==false){
        alert("Porfavor Completar formulario")
        return;
    }
    if($("#form_registro").valid()==true){
        alert('Bienvenido!  ');
        return;
        
    }
    
    let nombre = $("#nombre").val()
    let apellidos = $("#apellidos").val()
    let email1 = $("#email1").val()
    let password = $("#password").val()
    let password2 = $("#password2").val()
    let terminos = $("#terminos").is(":checked")
    
})