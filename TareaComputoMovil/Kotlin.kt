fun main() {
    val pinCorrecto = "1412"
    var intentosRestantes = 3
    println("Banco") 
    while (intentosRestantes > 0) {  
        println("Ingresa el pin karnal")
        val intento = readln()
        if (intento == pinCorrecto) {
            println("PIN correcto. Acceso concedido al sistema.")
            break 
        } else {
            intentosRestantes--
            
            if (intentosRestantes == 0) {
                println("Ha superado el límite de intentos. CUENTA BLOQUEADA.")
            }
        }
    }   
}