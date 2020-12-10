# © 2015 Oihane Crucelaegui - AvanzOSC
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models
#hola
class SeveralFields(models.Model):
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.manipulate.many2many'
class SeveralFields(models.Model):
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.manipulate.many2many2'
class SeveralFields(models.Model):
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.manipulate.many2many3'
class SeveralFields(models.Model):
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.manipulate.many2many4'
class modelo72form(models.Model):
    _description = 'Modelo para Manipular Many2many72'
    _name = 'model.many2many72'

    name = fields.Char('72form')
    
class modelo73form(models.Model):
    _description = 'Modelo para Manipular Many2many73'
    _name = 'model.many2many73'

    name = fields.Char('73form')


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    notes = fields.Html()
    #diseño
    x_diseño = fields.Boolean(string="Diseño",)
    x_tama_cli = fields.Char(string="Tamaño cliente",help="",)
    nuerevi = fields.Selection([('50', 'Nuevo'),('51', 'Reimpresion'),], "Tipo de trabajo",)
    tiene_cambio = fields.Selection([('50', 'Si'),('51', 'No'),], "Tiene cambio",)
    Cual_cambio = fields.Char(string="¿Cual cambio?",help="",)
    Numero_de_hojas = fields.Char(string="# Hojas",help="",)
    Tamaños_para_el_Pedido = fields.Char(string="Tamaños para el Pedido",help="",)
    Tamaños_Programados = fields.Char(string="Tamaños Programados",help="",)
    Copias_y_secuencia_de_color = fields.Char(string="Copias y secuencia de color",help="",)
    Sanduchar = fields.Boolean(string="Sanduchar",)
    Sanduchar_Pasta_Semidura = fields.Boolean(string="Sanduchar Pasta Semidura",)
    Sanduchar_Pasta_Dura = fields.Boolean(string="Sanduchar Pasta Dura",)
    Sanduchar_Pasta_Dura_con_lomo = fields.Boolean(string="Sanduchar Pasta Dura con lomo",)
    Sanduchar_Servicio_Pasta_Semidura = fields.Boolean(string="Sanduchar Servicio Pasta Semidura",)
    Sanduchar_Servicio_Pasta_Dura = fields.Boolean(string="Sanduchar Servicio Pasta Dura",)
    Sanduchar_Servicio_Pasta_Dura_con_lomo = fields.Boolean(string="Sanduchar Servicio Pasta Dura con lomo",)
    Sanduchar_Magnetica = fields.Boolean(string="Sanduchar Magnetica",)
    Argollado = fields.Boolean(string="Argollado",)
    Encuadernacion = fields.Boolean(string="Encuadernación",)
    Cinta_Cabezada = fields.Boolean(string="Cinta Cabezada",)
    Cosido_Hilo = fields.Boolean(string="Cosido Hilo",)
    Despunte_Tacos_carton = fields.Boolean(string="Despunte Tacos y carton",)
    Emblocado = fields.Boolean(string="Emblocado",)
    Gancho_Caballete = fields.Boolean(string="Gancho Caballete",)
    Hot_Melt = fields.Boolean(string="Hot Melt",)
    Iman = fields.Boolean(string="Iman",)
    Montaje_Guardas = fields.Boolean(string="Montaje del Libro y las Guardas",)
    Perforacion_para_Iman = fields.Boolean(string="Perforacion para Iman",)
    Resorte_Montaje = fields.Boolean(string="Resorte y Montaje",)
    Procesos_Varios = fields.Boolean(string="Procesos Varios",)
    Argollar = fields.Boolean(string="Argollar",)
    Armar_Sobre = fields.Boolean(string="Armar Sobre",)
    Descolillar = fields.Boolean(string="Descolillar",)
    Despuntar = fields.Boolean(string="Despuntar",)
    Grapar = fields.Boolean(string="Grapar",)
    Levantar = fields.Boolean(string="Levantar",)
    Levantar_Servicio = fields.Boolean(string="Levantar Servicio",)
    PegadoBolsillo = fields.Boolean(string="Pegado de Bolsillo",)
    Pegar_Adhesivo = fields.Boolean(string="Pegar Adhesivo",)
    Perforar_Taladro = fields.Boolean(string="Perforar Taladro",)
    Plegar = fields.Boolean(string="Perforar Taladro",)
    Revisar = fields.Boolean(string="Perforar Taladro",)
    Otros = fields.Char(string="Otros",help="",)
    # Montaje 
    tamasoporte = fields.Selection(
        [('50', '14x20'),
         ('51', '14x22'),
         ('52', '16,5x17,5'),
         ('53', '16,5x23'),
         ('54', '17,5x20'),
         ('55', '17,5x25'),
         ('56', '17,5x33'),
         ('57', '20x23'),
         ('58', '20x35'),
         ('59', '22x28'),
         ('1', '23x25'),
         ('2', '23x33'),
         ('3', '23x50'),
         ('4', '25x35'),
         ('5', '25x45'),
         ('6', '25x50'),
         ('7', '25x60'),
         ('8', '25x64'),
         ('9', '25x70'),
         ('10', '27x43'),
         ('11', '28x42'),
         ('12', '29x41'),
         ('13', '30x40'),
         ('14', '30x45'),
         ('15', '30x60'),
         ('16', '33x35'),
         ('17', '33x60'),
         ('18', '33x64'),
         ('19', '33x70'),
         ('20', '35x50'),
         ('21', '35x64'),
         ('22', '35x65'),
         ('23', '45x60'),
         ('24', '48x64'),
         ('15', '50x70'),
         ('16', '60x90'),
         ('17', '70x100'),
        ], "Tamaño pliego",
    )

    tintas_1 = fields.Selection(
        [('50', 'CMYK'),
         ('51', 'Cian'),
         ('52', 'Magenta'),
         ('53', 'Amarillo'),
         ('54', 'Negro'),
         ('56', 'Pantone'),
         ('55', 'Otro'),
         ], "Tintas",
    )

    tintas = fields.Selection(
        [('50', '4x0'),
         ('51', '4x1'),
         ('52', '4x2'),
         ('53', '4x3'),
         ('54', '4x4'),
         ('55', '3x0'),
         ('56', '3x1'),
         ('57', '3x2'),
         ('58', '3x3'),
         ('59', '2x0'),
         ('0', '2x1'),
         ('1', '2x2'),
         ('2', '1x0'),
         ('3', '1x1'),
         ('4', '5x0'),
         ('5', '5x1'),
         ('6', '5x2'),
         ('7', '5x3'),
         ('8', '5x4')
        ], "No Tintas",
    )

    x_merc72_form = fields.Many2many('model.many2many72', string="Codigos Pantone 1")
    x_merc73_form = fields.Many2many('model.many2many73', string="Codigos Pantone 2")


    codigos_Pantone = fields.Many2many('model.manipulate.many2many', string = "Codigos Pantone 1")
    codigos_Pantone2 = fields.Many2many('model.manipulate.many2many2', string = "Codigos Pantone 2")
    codigos_Pantone3 = fields.Many2many('model.manipulate.many2many3', string = "Codigos Pantone 3")
    codigos_Pantone4 = fields.Many2many('model.manipulate.many2many4', string = "Codigos Pantone 4")
    Barniz = fields.Selection(
        [('50', 'Sobreimpresion'),
         ('51', 'Acuoso'),
         ('52', 'No'),
         ], "Barniz",
    )
    tamaplancha = fields.Selection(
        [('50', 'Gto Cuarto'),
         ('51', 'Cuarto Mayor'),
         ('52', 'Medio Pliego'),
         ('53', 'Pliego'),
        ], "Tamaño plancha",
    )
    maquina = fields.Selection(
        [('50', 'Gto #1'),
         ('51', 'Adast # 2'),
         ('52', 'Medio Pliego'),
         ('53', 'Pliego'),
        ], "Maquina",
    )
    cavidadtroquel = fields.Selection(
        [('50', '1'),
         ('51', '2'),
         ('1', '3'),
         ('2', '4'),
         ('3', '5'),
         ('4', '6'),
         ('5', '7'),
         ('6', '8'),
         ('7', '9'),
         ('8', '10'),
         ('9', '11'),
         ('10', '12'),
         ('58', '13'),
         ('5911111', '14'),
         ('0', '15'),
         ('11', '16'),
         ('21', '17'),
         ('31', '18'),
         ('41', '19'),
         ('52', '20'),
         ('61', '21'),
         ('71', '22'),
         ('81', '23'),
         ('501', '24'),
         ('511222', '25'),
         ('111', '26'),
         ('211', '27'),
         ('311', '28'),
         ('411', '29'),
         ('511', '30'),
         ('611', '31'),
         ('711', '32'),
         ('811', '33'),
         ('911', '34'),
         ('1011', '35'),
         ('5811', '36'),
         ('59', '37'),
         ('011', '38'),
         ('1111', '39'),
         ('2111', '40'),
         ('3111', '41'),
         ('4111', '42'),
         ('5211', '43'),
         ('6111', '44'),
         ('7111', '45'),
         ('8111', '46'),
         ('52111', '47'),
         ('61111', '48'),
         ('71111', '49'),
         ('81111', '50'),
        ], "Cavidades Montaje",
    )
    Sangrado = fields.Selection(
        [('50', '0.5'),
         ('51', '1.0'),
         ('52', '1.5'),
         ('53', '2.0'),
        ], "Sangrado",
    )
    Montaje = fields.Selection(
        [('50', 'Tiro / Retiro'),
         ('51', 'Tiro & Retiro'),
         ('52', 'Montaje por Puntas'),
        ], "Montaje",
    )
    Giro_1 = fields.Selection(
        [('50', 'Escuadra'),
         ('51', 'Pinza'),
        ], "Giro",
    )
    Pelicula_UV = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),
        ], "Pelicula UV",
    )
    troquel = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),
        ], "Troquel",
    )
    cavidadtroquel = fields.Selection(
        [('50', '1'),
         ('51', '2'),
         ('1', '3'),
         ('2', '4'),
         ('3', '5'),
         ('4', '6'),
         ('5', '7'),
         ('6', '8'),
         ('7', '9'),
         ('8', '10'),
         ('9', '11'),
         ('10', '12'),
         ('58', '13'),
         ('5911111', '14'),
         ('0', '15'),
         ('11', '16'),
         ('21', '17'),
         ('31', '18'),
         ('41', '19'),
         ('52', '20'),
        ], "Cavidades troquel",
    )
    Clisse = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),
        ], "Clisse",
    )
    Cavidades_Clisse = fields.Selection(
        [('50', '1'),
         ('51', '2'),
         ('1', '3'),
         ('2', '4'),
         ('3', '5'),
         ('4', '6'),
         ('5', '7'),
         ('6', '8'),
         ('7', '9'),
         ('8', '10'),
         ('9', '11'),
         ('10', '12'),
         ('58', '13'),
         ('5911111', '14'),
         ('0', '15'),
         ('11', '16'),
         ('21', '17'),
         ('31', '18'),
         ('41', '19'),
         ('52', '20'),
        ], "Cavidades Clisse",
    )
    Clase_de_Clisse = fields.Selection(
        [('50', 'Estampado'),
         ('51', 'Repuje'),
        ], "Clase de Clisse",
    )
    tipo_papel = fields.Many2one(
        'product.product',string="Tipo de papel"
    )
    tamamateriprima = fields.Selection(
        [('50', '70x100	'),
         ('51', '60x90	'),
        ], "Tamaño papel",
    )
    tamasoporte = fields.Selection(
        [('50', '14x20'),
         ('51', '14x22'),
         ('52', '16,5x17,5'),
         ('53', '16,5x23'),
         ('54', '17,5x20'),
         ('55', '17,5x25'),
         ('56', '17,5x33'),
         ('57', '20x23'),
         ('58', '20x35'),
         ('59', '22x28'),
         ('1', '23x25'),
         ('2', '23x33'),
         ('3', '23x50'),
         ('4', '25x35'),
         ('5', '25x45'),
         ('6', '25x50'),
         ('7', '25x60'),
         ('8', '25x64'),
         ('9', '25x70'),
         ('10', '27x43'),
         ('11', '28x42'),
         ('12', '29x41'),
         ('13', '30x40'),
         ('14', '30x45'),
         ('15', '30x60'),
         ('16', '33x35'),
         ('17', '33x60'),
         ('18', '33x64'),
         ('19', '33x70'),
         ('20', '35x50'),
         ('21', '35x64'),
         ('22', '35x65'),
         ('23', '45x60'),
         ('24', '48x64'),
         ('15', '50x70'),
         ('16', '60x90'),
         ('17', '70x100'),
        ], "Tamaño pliego",
    )
    Es_Talonario = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),
        ], "Es Talonario",
    )
    Laminados = fields.Selection(
        [('50', 'Laminado Brillante 1 Cara'),
         ('51', 'Laminado Brillante 2 Cara'),
         ('52', 'Laminado Mate 1 Cara'),
         ('53', 'Laminado Mate 2 Cara'),
         ('16', 'Metalizado'),
         ('17', 'Polipropileno Duro'),
        ], "Laminados",
    )

    Barniz_UV = fields.Selection(
        [('50', 'Barniz UV Reserva 1 Cara'),
         ('51', 'Barniz UV Reserva 2 Cara'),
         ('52', 'Barniz UV Total 1 Cara'),
         ('53', 'Barniz UV Total 1 Cara'),
        ], "Barniz UV",
    )
    Clase_Barniz_UV = fields.Selection(
        [('50', 'Normal'),
         ('51', 'Soft Toch'),
         ('52', 'Alto Relieve'),
         ('53', 'Anti Crash'),
        ], "Clase Barniz UV",
    )
    Troquelado = fields.Selection(
        [('50', 'Grafado'),
         ('51', 'Pretroquelado'),
         ('52', 'Troquelado'),
        ], "Troquelado",
    )
    EstampadoRepuje = fields.Selection(
        [('50', 'Hot Stamping'),
         ('51', 'Repujado'),
        ], "Estampado - Repuje",
    )
    Talonario = fields.Selection(
        [('50', 'Numerado y Terminado'),
         ('51', 'Emblocado'),
         ('52', 'Emblocado-Levantado'),
         ('53', 'Numerado'),
         ('16', 'Numerado - Perforado'),
         ('17', 'Perforado'),
        ], "Talonario",
    )
    Tapa_talonario = fields.Selection(
        [('50', 'Tapa Carton'),
         ('51', 'Tapa Manila'),
        ], "Tapa talonario",
    )


