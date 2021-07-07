class pacient():
    def __init__(self, db, pac_id, pac_nome, pac_email, pac_celular, pac_senha, pac_CPF, pac_nascimento, pac_endereco, psi_id, p_list):
        self.db = db
        self.pac_id = pac_id
        self.pac_nome = pac_nome
        self.pac_email = pac_email
        self.pac_celular = pac_celular
        self.pac_senha = pac_senha
        self.pac_CPF = pac_CPF
        self.pac_nascimento = pac_nascimento
        self.pac_endereco = pac_endereco
        self.psi_id = psi_id
        self.p_list = p_list
        
    def post(self):
        return self.db.cursor.execute(f"""INSERT INTO `paciente`(
        `pac_nome`,
        `pac_email`,
        `pac_celular`,
        `pac_senha`,
        `pac_CPF`,
        `pac_nascimento`,
        `pac_endereco`,
        `psi_id`,
        `P1`,
        `P2`,
        `P3`,
        `P4`,
        `P5`,
        `P6`,
        `P7`,
        `P8`,
        `P9`,
        `P12`,
        `P13`,
        `P14`,
        `P15`,
        `P16`,
        `P17`,
        `P18`,
        `P19`,
        `P20`,
        `P21`,
        `P22`,
        `P23`,
        `P24`,
        `P25`,
        `P26`,
        `P27`,
        `P28`,
        `P29`,
        `P30`,
        `P31`,
        `P32`,
        `P33`,
        `P34`,
        `P35`,
        `P36`,
        `P37`,
        `P38`,
        `P39`,
        `P40`,
        `P41`,
        `P42`) VALUES(
        {self.pac_nome},
        {self.pac_email},
        {self.pac_celular},
        {self.pac_senha},
        {self.pac_CPF},
        {self.pac_nascimento},
        {self.pac_endereco},
        {self.psi_id},
        {self.p_list[1]},
        {self.p_list[2]},
        {self.p_list[3]},
        {self.p_list[4]},
        {self.p_list[5]},
        {self.p_list[6]},
        {self.p_list[7]},
        {self.p_list[8]},
        {self.p_list[9]},
        {self.p_list[10]},
        {self.p_list[11]},
        {self.p_list[12]},
        {self.p_list[13]},
        {self.p_list[14]},
        {self.p_list[15]},
        {self.p_list[16]},
        {self.p_list[17]},
        {self.p_list[18]},
        {self.p_list[19]},
        {self.p_list[20]},
        {self.p_list[21]},
        {self.p_list[22]},
        {self.p_list[23]},
        {self.p_list[24]},
        {self.p_list[25]},
        {self.p_list[26]},
        {self.p_list[27]},
        {self.p_list[28]},
        {self.p_list[29]},
        {self.p_list[30]},
        {self.p_list[31]},
        {self.p_list[32]},
        {self.p_list[33]},
        {self.p_list[34]},
        {self.p_list[35]},
        {self.p_list[36]},
        {self.p_list[37]},
        {self.p_list[38]},
        {self.p_list[39]},
        {self.p_list[40]},
        {self.p_list[41]},
        {self.p_list[42]});""")

    def get(self):
        return self.db.cursor.execute(f"""SELECT * FROM paciente;""")