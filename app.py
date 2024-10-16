import sqlite3
import os
from flask import Flask, render_template, request, g, flash, redirect, url_for, session
from datetime import timedelta
import math


from FDataBase import FDataBase

DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'fglkhfdshfiuiudsfkjvifgiuspinvjkoie'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))
app.permanent_session_lifetime = timedelta(minutes=100)

def login_admin():
    session.permanent = True
    session['admin_logged'] = 1

def isLogged():
    return True if session.get('admin_logged') else False

def logout_admin():
    session.pop('admin_logged', None)

# //////////////////////////////////

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'], check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

dbase = None
@app.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = FDataBase(db)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        g.link_db.close()

# //////////////////////////////////

POSTS_PER_PAGE = 12  # Number of posts per page

@app.route('/', methods=['POST', 'GET'])
@app.route('/page/<int:page>', methods=['POST', 'GET'])  # Allow navigating to specific pages
def index(page=1):
    offset = (page - 1) * POSTS_PER_PAGE  # Calculate the offset for the query
    total_posts = dbase.getPostCount()  # Total number of posts
    total_pages = math.ceil(total_posts / POSTS_PER_PAGE)  # Total number of pages

    # Handle adding new posts (if POST request)
    if request.method == 'POST':
            if len(request.form['cat']) > 1:
                res = dbase.addPost(request.form['title'], request.form['img'], request.form['cat'],
                                    request.form['title_0'], request.form['text_00'], request.form['text_01'], request.form['text_02'], request.form['text_03'], request.form['text_04'], request.form['text_05'], request.form['text_06'], request.form['text_07'], request.form['text_08'], request.form['text_09'], request.form['img_01'], request.form['img_02'], request.form['img_03'], request.form['img_04'], request.form['img_05'], request.form['img_06'],
                                    request.form['title_1'], request.form['text_10'], request.form['text_11'], request.form['text_12'], request.form['text_13'], request.form['text_14'], request.form['text_15'], request.form['text_16'], request.form['text_17'], request.form['text_18'], request.form['text_19'], request.form['img_11'], request.form['img_12'], request.form['img_13'], request.form['img_14'], request.form['img_15'], request.form['img_16'],
                                    request.form['title_2'], request.form['text_20'], request.form['text_21'], request.form['text_22'], request.form['text_23'], request.form['text_24'], request.form['text_25'], request.form['text_26'], request.form['text_27'], request.form['text_28'], request.form['text_29'], request.form['img_21'], request.form['img_22'], request.form['img_23'], request.form['img_24'], request.form['img_25'], request.form['img_26'],
                                    request.form['title_3'], request.form['text_30'], request.form['text_31'], request.form['text_32'], request.form['text_33'], request.form['text_34'], request.form['text_35'], request.form['text_36'], request.form['text_37'], request.form['text_38'], request.form['text_39'], request.form['img_31'], request.form['img_32'], request.form['img_33'], request.form['img_34'], request.form['img_35'], request.form['img_36'],
                                    request.form['title_4'], request.form['text_40'], request.form['text_41'], request.form['text_42'], request.form['text_43'], request.form['text_44'], request.form['text_45'], request.form['text_46'], request.form['text_47'], request.form['text_48'], request.form['text_49'], request.form['img_41'], request.form['img_42'], request.form['img_43'], request.form['img_44'], request.form['img_45'], request.form['img_46'],
                                    request.form['title_5'], request.form['text_50'], request.form['text_51'], request.form['text_52'], request.form['text_53'], request.form['text_54'], request.form['text_55'], request.form['text_56'], request.form['text_57'], request.form['text_58'], request.form['text_59'], request.form['img_51'], request.form['img_52'], request.form['img_53'], request.form['img_54'], request.form['img_55'], request.form['img_56'],
                                    request.form['title_6'], request.form['text_60'], request.form['text_61'], request.form['text_62'], request.form['text_63'], request.form['text_64'], request.form['text_65'], request.form['text_66'], request.form['text_67'], request.form['text_68'], request.form['text_69'], request.form['img_61'], request.form['img_62'], request.form['img_63'], request.form['img_64'], request.form['img_65'], request.form['img_66'],
                                    request.form['title_7'], request.form['text_70'], request.form['text_71'], request.form['text_72'], request.form['text_73'], request.form['text_74'], request.form['text_75'], request.form['text_76'], request.form['text_77'], request.form['text_78'], request.form['text_79'], request.form['img_71'], request.form['img_72'], request.form['img_73'], request.form['img_74'], request.form['img_75'], request.form['img_76'],
                                    request.form['title_8'], request.form['text_80'], request.form['text_81'], request.form['text_82'], request.form['text_83'], request.form['text_84'], request.form['text_85'], request.form['text_86'], request.form['text_87'], request.form['text_88'], request.form['text_89'], request.form['img_81'], request.form['img_82'], request.form['img_83'], request.form['img_84'], request.form['img_85'], request.form['img_86'],
                                    request.form['title_9'], request.form['text_90'], request.form['text_91'], request.form['text_92'], request.form['text_93'], request.form['text_94'], request.form['text_95'], request.form['text_96'], request.form['text_97'], request.form['text_98'], request.form['text_99'], request.form['img_91'], request.form['img_92'], request.form['img_93'], request.form['img_94'], request.form['img_95'], request.form['img_96']
                                    )
                
                if res:
                    flash("Post Added", category='success')
                else:
                    flash("Post Not Added", category='error')
            else:
                flash("Select Category", category='error')

    # Fetch posts for the current page
    posts = dbase.getPostAnonce(POSTS_PER_PAGE, offset)
    count = dbase.getPostCount()

    return render_template('index.html', posts=posts, login=isLogged(), page=page, total_pages=total_pages, index=index, count=count)

@app.route('/category/<path:cat>', methods=['POST', 'GET'])  # Ensure cat is treated as an integer
@app.route('/category/<path:cat>/page/<int:page>', methods=['POST', 'GET'])  # Add pagination to category view
def category(cat, page=1):
    offset = (page - 1) * POSTS_PER_PAGE
    total_posts = dbase.getCategoryPostCount(cat)  # Total number of posts in this category
    total_pages = math.ceil(total_posts / POSTS_PER_PAGE)

    if request.method == 'POST':
            if len(request.form['cat']) > 1:
                res = dbase.addPost(request.form['title'], request.form['img'], request.form['cat'],
                                    request.form['title_0'], request.form['text_00'], request.form['text_01'], request.form['text_02'], request.form['text_03'], request.form['text_04'], request.form['text_05'], request.form['text_06'], request.form['text_07'], request.form['text_08'], request.form['text_09'], request.form['img_01'], request.form['img_02'], request.form['img_03'], request.form['img_04'], request.form['img_05'], request.form['img_06'],
                                    request.form['title_1'], request.form['text_10'], request.form['text_11'], request.form['text_12'], request.form['text_13'], request.form['text_14'], request.form['text_15'], request.form['text_16'], request.form['text_17'], request.form['text_18'], request.form['text_19'], request.form['img_11'], request.form['img_12'], request.form['img_13'], request.form['img_14'], request.form['img_15'], request.form['img_16'],
                                    request.form['title_2'], request.form['text_20'], request.form['text_21'], request.form['text_22'], request.form['text_23'], request.form['text_24'], request.form['text_25'], request.form['text_26'], request.form['text_27'], request.form['text_28'], request.form['text_29'], request.form['img_21'], request.form['img_22'], request.form['img_23'], request.form['img_24'], request.form['img_25'], request.form['img_26'],
                                    request.form['title_3'], request.form['text_30'], request.form['text_31'], request.form['text_32'], request.form['text_33'], request.form['text_34'], request.form['text_35'], request.form['text_36'], request.form['text_37'], request.form['text_38'], request.form['text_39'], request.form['img_31'], request.form['img_32'], request.form['img_33'], request.form['img_34'], request.form['img_35'], request.form['img_36'],
                                    request.form['title_4'], request.form['text_40'], request.form['text_41'], request.form['text_42'], request.form['text_43'], request.form['text_44'], request.form['text_45'], request.form['text_46'], request.form['text_47'], request.form['text_48'], request.form['text_49'], request.form['img_41'], request.form['img_42'], request.form['img_43'], request.form['img_44'], request.form['img_45'], request.form['img_46'],
                                    request.form['title_5'], request.form['text_50'], request.form['text_51'], request.form['text_52'], request.form['text_53'], request.form['text_54'], request.form['text_55'], request.form['text_56'], request.form['text_57'], request.form['text_58'], request.form['text_59'], request.form['img_51'], request.form['img_52'], request.form['img_53'], request.form['img_54'], request.form['img_55'], request.form['img_56'],
                                    request.form['title_6'], request.form['text_60'], request.form['text_61'], request.form['text_62'], request.form['text_63'], request.form['text_64'], request.form['text_65'], request.form['text_66'], request.form['text_67'], request.form['text_68'], request.form['text_69'], request.form['img_61'], request.form['img_62'], request.form['img_63'], request.form['img_64'], request.form['img_65'], request.form['img_66'],
                                    request.form['title_7'], request.form['text_70'], request.form['text_71'], request.form['text_72'], request.form['text_73'], request.form['text_74'], request.form['text_75'], request.form['text_76'], request.form['text_77'], request.form['text_78'], request.form['text_79'], request.form['img_71'], request.form['img_72'], request.form['img_73'], request.form['img_74'], request.form['img_75'], request.form['img_76'],
                                    request.form['title_8'], request.form['text_80'], request.form['text_81'], request.form['text_82'], request.form['text_83'], request.form['text_84'], request.form['text_85'], request.form['text_86'], request.form['text_87'], request.form['text_88'], request.form['text_89'], request.form['img_81'], request.form['img_82'], request.form['img_83'], request.form['img_84'], request.form['img_85'], request.form['img_86'],
                                    request.form['title_9'], request.form['text_90'], request.form['text_91'], request.form['text_92'], request.form['text_93'], request.form['text_94'], request.form['text_95'], request.form['text_96'], request.form['text_97'], request.form['text_98'], request.form['text_99'], request.form['img_91'], request.form['img_92'], request.form['img_93'], request.form['img_94'], request.form['img_95'], request.form['img_96']
                                    )
                
                if res:
                    flash("Post Added", category='success')
                else:
                    flash("Post Not Added", category='error')
            else:
                flash("Select Category", category='error')

    # Fetch posts for the current page and category
    posts = dbase.catPost(cat, POSTS_PER_PAGE, offset)
    count = dbase.getCategoryPostCount(cat)

    # Pass the category as an integer to the template
    return render_template('index.html', posts=posts, login=isLogged(), page=page, total_pages=total_pages, category=cat, count=count)

@app.route('/update/<int:id>', methods=['POST', 'GET'])
@app.route('/update/category/<path:cat>/<int:id>', methods=['POST', 'GET'])
def changePost(cat=None, id=None):
    if not isLogged():
        return redirect(url_for('login'))

    post = dbase.getPost(id)

    if request.method == 'POST':
            if len(request.form['cat']) > 1:

            # Updating the post
                res = dbase.changePost(
                    post['id'], request.form['title'], request.form['img'], request.form['cat'],
                                    request.form['title_0'], request.form['text_00'], request.form['text_01'], request.form['text_02'], request.form['text_03'], request.form['text_04'], request.form['text_05'], request.form['text_06'], request.form['text_07'], request.form['text_08'], request.form['text_09'], request.form['img_01'], request.form['img_02'], request.form['img_03'], request.form['img_04'], request.form['img_05'], request.form['img_06'],
                                    request.form['title_1'], request.form['text_10'], request.form['text_11'], request.form['text_12'], request.form['text_13'], request.form['text_14'], request.form['text_15'], request.form['text_16'], request.form['text_17'], request.form['text_18'], request.form['text_19'], request.form['img_11'], request.form['img_12'], request.form['img_13'], request.form['img_14'], request.form['img_15'], request.form['img_16'],
                                    request.form['title_2'], request.form['text_20'], request.form['text_21'], request.form['text_22'], request.form['text_23'], request.form['text_24'], request.form['text_25'], request.form['text_26'], request.form['text_27'], request.form['text_28'], request.form['text_29'], request.form['img_21'], request.form['img_22'], request.form['img_23'], request.form['img_24'], request.form['img_25'], request.form['img_26'],
                                    request.form['title_3'], request.form['text_30'], request.form['text_31'], request.form['text_32'], request.form['text_33'], request.form['text_34'], request.form['text_35'], request.form['text_36'], request.form['text_37'], request.form['text_38'], request.form['text_39'], request.form['img_31'], request.form['img_32'], request.form['img_33'], request.form['img_34'], request.form['img_35'], request.form['img_36'],
                                    request.form['title_4'], request.form['text_40'], request.form['text_41'], request.form['text_42'], request.form['text_43'], request.form['text_44'], request.form['text_45'], request.form['text_46'], request.form['text_47'], request.form['text_48'], request.form['text_49'], request.form['img_41'], request.form['img_42'], request.form['img_43'], request.form['img_44'], request.form['img_45'], request.form['img_46'],
                                    request.form['title_5'], request.form['text_50'], request.form['text_51'], request.form['text_52'], request.form['text_53'], request.form['text_54'], request.form['text_55'], request.form['text_56'], request.form['text_57'], request.form['text_58'], request.form['text_59'], request.form['img_51'], request.form['img_52'], request.form['img_53'], request.form['img_54'], request.form['img_55'], request.form['img_56'],
                                    request.form['title_6'], request.form['text_60'], request.form['text_61'], request.form['text_62'], request.form['text_63'], request.form['text_64'], request.form['text_65'], request.form['text_66'], request.form['text_67'], request.form['text_68'], request.form['text_69'], request.form['img_61'], request.form['img_62'], request.form['img_63'], request.form['img_64'], request.form['img_65'], request.form['img_66'],
                                    request.form['title_7'], request.form['text_70'], request.form['text_71'], request.form['text_72'], request.form['text_73'], request.form['text_74'], request.form['text_75'], request.form['text_76'], request.form['text_77'], request.form['text_78'], request.form['text_79'], request.form['img_71'], request.form['img_72'], request.form['img_73'], request.form['img_74'], request.form['img_75'], request.form['img_76'],
                                    request.form['title_8'], request.form['text_80'], request.form['text_81'], request.form['text_82'], request.form['text_83'], request.form['text_84'], request.form['text_85'], request.form['text_86'], request.form['text_87'], request.form['text_88'], request.form['text_89'], request.form['img_81'], request.form['img_82'], request.form['img_83'], request.form['img_84'], request.form['img_85'], request.form['img_86'],
                                    request.form['title_9'], request.form['text_90'], request.form['text_91'], request.form['text_92'], request.form['text_93'], request.form['text_94'], request.form['text_95'], request.form['text_96'], request.form['text_97'], request.form['text_98'], request.form['text_99'], request.form['img_91'], request.form['img_92'], request.form['img_93'], request.form['img_94'], request.form['img_95'], request.form['img_96']
                                    )

                if res:
                    flash("Post Updated", category='success')
                else:
                    flash('Post Not Updated', category='error')
            else:
                flash("Select Category", category='error')

    if cat:
        return redirect(url_for("category", cat=cat))
    else:
        return redirect(url_for("index"))
    
@app.route('/delete/<int:id>', methods=['POST', 'GET'])
@app.route('/delete/category/<path:cat>/<int:id>', methods=['POST', 'GET'])
def deletePost(cat=None, id=None):
    if not isLogged():
        return redirect(url_for('login'))
    
    post = dbase.getPost(id)
    res = dbase.deletePost(post['id'])
        
    if res:
        flash("Post Deleted", category='success')
    else:
        flash('Post Not Deleted', category='error')

    if cat:
        return redirect(url_for("category", cat=cat))
    else:
        return redirect(url_for("index"))

@app.errorhandler(404)
def error(e): 
    return redirect(url_for("index"))

@app.route('/see', methods=['POST', 'GET'])
@app.route('/see/page/<int:page>', methods=['POST', 'GET'])  # Allow navigating to specific pages
def see(page=1):
    offset = (page - 1) * POSTS_PER_PAGE  # Calculate the offset for the query
    
    total_posts = dbase.getPostCount()  # Total number of posts
    total_pages = math.ceil(total_posts / POSTS_PER_PAGE)  # Total number of pages
    posts = dbase.getPostAnonce(POSTS_PER_PAGE, offset)

    flash("User See", category = 'success')

    return render_template('see.html', posts=posts, login=isLogged(), page=page, total_pages=total_pages, see=see)

@app.route('/post/<id>', methods=['POST', 'GET'])
def post(id):
    
    post = dbase.getPost(id)
    posts = dbase.getPostAnonce()

    return render_template('post.html', p=post, posts=posts)
# //////////////////////////////////

@app.route("/login", methods=['POST', 'GET'])
def login(): 
    if isLogged():
        return redirect(url_for("index"))

    if request.method == 'POST':
        if request.form['name'] == 'Login or Password is incorrect' and request.form['psw'] == 'Login or Password is incorrect':
            login_admin()

            if login_admin:
                flash("Logged in", category='success')
                return redirect(url_for("index"))
            
        else:   
            flash('Login or Password is incorrect', category='error')

    return render_template('login.html')

@app.route('/logout')
def logout():

    if isLogged():
        logout_admin()
        flash('Logged out', category='success')
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)