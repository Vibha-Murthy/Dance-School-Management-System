# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YES",
    database="pes1ug20cs495_danceschool"
)
c = mydb.cursor(buffered=True)

#ADD DATA INTO TABLES
def add_data_musician(musician_id, musician_name, musician_instr, musician_band_id):
    c.execute('INSERT INTO Musician VALUES (%s,%s,%s,%s)',
              (musician_id, musician_name, musician_instr, musician_band_id))
    mydb.commit()

def add_data_band(band_id, band_name):
    c.execute('INSERT INTO Music_Band VALUES (%s,%s)',
              (band_id, band_name))
    mydb.commit()

def add_data_costume(C_ID, costume, avail, qty, store):
    c.execute('INSERT INTO Costume VALUES (%s,%s,%s,%s,%s)',
              (C_ID, costume, avail, qty, store))
    mydb.commit()

def add_data_dancestyle(d_ID, style):
    c.execute('INSERT INTO Dance_Style VALUES (%s,%s)',
              (d_ID, style))
    mydb.commit()

def add_data_danceschool(s_ID, schname, srtdt, loc):
    c.execute('INSERT INTO Dance_School VALUES (%s,%s,%s,%s)',
              (s_ID, schname, srtdt, loc))
    mydb.commit()

def add_data_batch(b_ID, hw, s_ID):
    c.execute('INSERT INTO Batch VALUES (%s,%s,%s)',
              (b_ID, hw, s_ID))
    mydb.commit()

def add_data_trainer(t_ID, trnname, phn, d_ID, b_ID):
    c.execute('INSERT INTO Trainer VALUES (%s,%s,%s,%s,%s)',
              (t_ID, trnname, phn, d_ID, b_ID))
    mydb.commit()

def add_data_student(std_ID, f_name, l_name, jndt, dur, dob, addr, b_ID, p_ID):
    c.execute('INSERT INTO Student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (std_ID, f_name, l_name, jndt, dur, dob, addr, b_ID, p_ID))
    mydb.commit()

def add_data_performance(p_ID,venue,date,style,song,c_ID,m_ID,t_ID):
    c.execute('INSERT INTO Performance VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
              (p_ID,venue,date,style,song,c_ID,m_ID,t_ID))
    mydb.commit()


#VIEW DATA IN TABLES
def view_all_performance():
    c.execute('SELECT * FROM Performance')
    data = c.fetchall()
    return data

def view_all_student():
    c.execute('SELECT * FROM Student')
    data = c.fetchall()
    return data

def view_all_musician():
    c.execute('SELECT * FROM Musician')
    data = c.fetchall()
    return data

def view_all_trainer():
    c.execute('SELECT * FROM Trainer')
    data = c.fetchall()
    return data

def view_all_costume():
    c.execute('SELECT * FROM Costume')
    data = c.fetchall()
    return data


def view_only_pid():
    c.execute('SELECT P_ID FROM Performance')
    data = c.fetchall()
    return data

def view_only_muid():
    c.execute('SELECT Mu_ID FROM Musician')
    data = c.fetchall()
    return data

def view_only_stdid():
    c.execute('SELECT Std_ID FROM Student')
    data = c.fetchall()
    return data

def view_only_tid():
    c.execute('SELECT T_ID FROM Trainer')
    data = c.fetchall()
    return data


#DELETE DATA FROM TABLES
def delete_perf(pid):
    c.execute('DELETE FROM Performance WHERE P_ID="{}"'.format(pid))
    mydb.commit()

def delete_musi(muid):
    c.execute('DELETE FROM Musician WHERE MU_ID="{}"'.format(muid))
    mydb.commit()

def delete_train(tid):
    c.execute('DELETE FROM Trainer WHERE T_ID="{}"'.format(tid))
    mydb.commit()

def delete_stud(stdid):
    c.execute('DELETE FROM Student WHERE Std_ID="{}"'.format(stdid))
    mydb.commit()


#UPDATE DATA IN TABLES
def edit_perf_data(new_date, new_venue, pid):
    c.execute("UPDATE Performance SET date=%s, venue=%s WHERE P_ID=%s", (new_date, new_venue, pid))
    mydb.commit()


def edit_stud_data(duration, sid):
    c.execute("UPDATE Student SET duration=%s WHERE Std_ID=%s", (duration, sid))
    mydb.commit()


#Procedure
def edit_costume_data():
    c.execute("CALL restock();")
    mydb.commit()


#RUN QUERY
def query(q):
    c.execute(q)
    mydb.commit()
    data=c.fetchall()
    return data

#Get
def get_performance(pid):
    c.execute('SELECT * FROM Performance WHERE P_ID="{}"'.format(pid))
    data = c.fetchall()
    return data

def get_stud(stdid):
    c.execute('SELECT * FROM Student WHERE Std_ID="{}"'.format(stdid))
    data = c.fetchall()
    return data


#Aggregate
def stud_agg():
    c.execute("Select s.name, B_ID, count(*) from (student natural join batch) natural join dance_school as s group by name, B_ID;")
    data = c.fetchall()
    return data

#Join
def perf_join():
    c.execute("select p.P_ID, p.venue, p.Date, p.Style, p.Song, m.name, c.costume, c.availability, t.name, count(s.f_name) from (((performance as p natural join music_band as m) join costume as c on p.C_ID = c.C_ID) join trainer as t on p.T_ID = t.T_ID) join student as s on s.P_ID = p.P_ID group by p.P_ID;")
    data = c.fetchall()
    return data

#Function
def style_func(sy):
    c.execute("select s.Style, style({}), B_ID from trainer natural join dance_style as s where D_ID = {} group by s.Style;".format(sy,sy))
    data = c.fetchall()
    return data

