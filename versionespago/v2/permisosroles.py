
class ValidarRoles:
    rol_user=[]
    def __int__(self,usuario):
        self.usuario=usuario

    def isAdministrador(self):

        if self.usuario.rol=='AD':
            return  True

    def isNORMAL(self):

        if self.usuario.rol == 'NR':
            return True

    def isANONIMO(self):

        if self.usuario.rol == 'NR':
            return True