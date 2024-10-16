import sqlite3
import datetime


class FDataBase:
    def __init__(self, db):
        self.__db = db

    def addPost(self, title, img, cat, 
                title_0, text_00, text_01, text_02, text_03, text_04, text_05, text_06, text_07, text_08, text_09, img_01, img_02, img_03, img_04, img_05, img_06,
                title_1, text_10, text_11, text_12, text_13, text_14, text_15, text_16, text_17, text_18, text_19, img_11, img_12, img_13, img_14, img_15, img_16,
                title_2, text_20, text_21, text_22, text_23, text_24, text_25, text_26, text_27, text_28, text_29, img_21, img_22, img_23, img_24, img_25, img_26,
                title_3, text_30, text_31, text_32, text_33, text_34, text_35, text_36, text_37, text_38, text_39, img_31, img_32, img_33, img_34, img_35, img_36,
                title_4, text_40, text_41, text_42, text_43, text_44, text_45, text_46, text_47, text_48, text_49, img_41, img_42, img_43, img_44, img_45, img_46,
                title_5, text_50, text_51, text_52, text_53, text_54, text_55, text_56, text_57, text_58, text_59, img_51, img_52, img_53, img_54, img_55, img_56,
                title_6, text_60, text_61, text_62, text_63, text_64, text_65, text_66, text_67, text_68, text_69, img_61, img_62, img_63, img_64, img_65, img_66,
                title_7, text_70, text_71, text_72, text_73, text_74, text_75, text_76, text_77, text_78, text_79, img_71, img_72, img_73, img_74, img_75, img_76,
                title_8, text_80, text_81, text_82, text_83, text_84, text_85, text_86, text_87, text_88, text_89, img_81, img_82, img_83, img_84, img_85, img_86,
                title_9, text_90, text_91, text_92, text_93, text_94, text_95, text_96, text_97, text_98, text_99, img_91, img_92, img_93, img_94, img_95, img_96 ):
        
        try:
            tm = datetime.datetime.now()
            time = tm.strftime("%d.%m.%Y")

            cur = self.__db.cursor()  # Create a new cursor
            cur.execute('INSERT INTO posts VALUES(NULL, ?, ?, ?, ?, ?, \
                                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
                                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
                                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
                                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
                                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
                                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
                                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
                                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
                                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
                                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )', (title, img, cat, tm, time, 
                title_0, text_00, text_01, text_02, text_03, text_04, text_05, text_06, text_07, text_08, text_09, img_01, img_02, img_03, img_04, img_05, img_06,
                title_1, text_10, text_11, text_12, text_13, text_14, text_15, text_16, text_17, text_18, text_19, img_11, img_12, img_13, img_14, img_15, img_16,
                title_2, text_20, text_21, text_22, text_23, text_24, text_25, text_26, text_27, text_28, text_29, img_21, img_22, img_23, img_24, img_25, img_26,
                title_3, text_30, text_31, text_32, text_33, text_34, text_35, text_36, text_37, text_38, text_39, img_31, img_32, img_33, img_34, img_35, img_36,
                title_4, text_40, text_41, text_42, text_43, text_44, text_45, text_46, text_47, text_48, text_49, img_41, img_42, img_43, img_44, img_45, img_46,
                title_5, text_50, text_51, text_52, text_53, text_54, text_55, text_56, text_57, text_58, text_59, img_51, img_52, img_53, img_54, img_55, img_56,
                title_6, text_60, text_61, text_62, text_63, text_64, text_65, text_66, text_67, text_68, text_69, img_61, img_62, img_63, img_64, img_65, img_66,
                title_7, text_70, text_71, text_72, text_73, text_74, text_75, text_76, text_77, text_78, text_79, img_71, img_72, img_73, img_74, img_75, img_76,
                title_8, text_80, text_81, text_82, text_83, text_84, text_85, text_86, text_87, text_88, text_89, img_81, img_82, img_83, img_84, img_85, img_86,
                title_9, text_90, text_91, text_92, text_93, text_94, text_95, text_96, text_97, text_98, text_99, img_91, img_92, img_93, img_94, img_95, img_96 ))
            self.__db.commit()
            cur.close()  # Close the cursor after usage


        except sqlite3.Error as e:
            print('Errors adding post from db '+str(e))
            return False
        
        return True
    
    def getPostAnonce(self, limit=6, offset=0):
        """Fetch posts with pagination support."""
        try:
            cur = self.__db.cursor()  # Create a new cursor for fetching
            cur.execute(f"SELECT id, title, img, cat, tm, time, \
                               title_0, text_00, text_01, text_02, text_03, text_04, text_05, text_06, text_07, text_08, text_09, img_01, img_02, img_03, img_04, img_05, img_06, \
                               title_1, text_10, text_11, text_12, text_13, text_14, text_15, text_16, text_17, text_18, text_19, img_11, img_12, img_13, img_14, img_15, img_16, \
                               title_2, text_20, text_21, text_22, text_23, text_24, text_25, text_26, text_27, text_28, text_29, img_21, img_22, img_23, img_24, img_25, img_26, \
                               title_3, text_30, text_31, text_32, text_33, text_34, text_35, text_36, text_37, text_38, text_39, img_31, img_32, img_33, img_34, img_35, img_36, \
                               title_4, text_40, text_41, text_42, text_43, text_44, text_45, text_46, text_47, text_48, text_49, img_41, img_42, img_43, img_44, img_45, img_46, \
                               title_5, text_50, text_51, text_52, text_53, text_54, text_55, text_56, text_57, text_58, text_59, img_51, img_52, img_53, img_54, img_55, img_56, \
                               title_6, text_60, text_61, text_62, text_63, text_64, text_65, text_66, text_67, text_68, text_69, img_61, img_62, img_63, img_64, img_65, img_66, \
                               title_7, text_70, text_71, text_72, text_73, text_74, text_75, text_76, text_77, text_78, text_79, img_71, img_72, img_73, img_74, img_75, img_76, \
                               title_8, text_80, text_81, text_82, text_83, text_84, text_85, text_86, text_87, text_88, text_89, img_81, img_82, img_83, img_84, img_85, img_86, \
                               title_9, text_90, text_91, text_92, text_93, text_94, text_95, text_96, text_97, text_98, text_99, img_91, img_92, img_93, img_94, img_95, img_96 FROM posts ORDER BY tm DESC LIMIT {limit} OFFSET {offset}")
            res = cur.fetchall()
            cur.close()  # Close the cursor after the query

            if res: 
                return res
        except sqlite3.Error as e:
            print('Errors getting post from bd '+str(e))
        return []
    
    def getPost(self, id):
        try:
            cur = self.__db.cursor()  # Create a new cursor for fetching
            cur.execute(f'SELECT id, title, img, cat, tm, time, \
                               title_0, text_00, text_01, text_02, text_03, text_04, text_05, text_06, text_07, text_08, text_09, img_01, img_02, img_03, img_04, img_05, img_06, \
                               title_1, text_10, text_11, text_12, text_13, text_14, text_15, text_16, text_17, text_18, text_19, img_11, img_12, img_13, img_14, img_15, img_16, \
                               title_2, text_20, text_21, text_22, text_23, text_24, text_25, text_26, text_27, text_28, text_29, img_21, img_22, img_23, img_24, img_25, img_26, \
                               title_3, text_30, text_31, text_32, text_33, text_34, text_35, text_36, text_37, text_38, text_39, img_31, img_32, img_33, img_34, img_35, img_36, \
                               title_4, text_40, text_41, text_42, text_43, text_44, text_45, text_46, text_47, text_48, text_49, img_41, img_42, img_43, img_44, img_45, img_46, \
                               title_5, text_50, text_51, text_52, text_53, text_54, text_55, text_56, text_57, text_58, text_59, img_51, img_52, img_53, img_54, img_55, img_56, \
                               title_6, text_60, text_61, text_62, text_63, text_64, text_65, text_66, text_67, text_68, text_69, img_61, img_62, img_63, img_64, img_65, img_66, \
                               title_7, text_70, text_71, text_72, text_73, text_74, text_75, text_76, text_77, text_78, text_79, img_71, img_72, img_73, img_74, img_75, img_76, \
                               title_8, text_80, text_81, text_82, text_83, text_84, text_85, text_86, text_87, text_88, text_89, img_81, img_82, img_83, img_84, img_85, img_86, \
                               title_9, text_90, text_91, text_92, text_93, text_94, text_95, text_96, text_97, text_98, text_99, img_91, img_92, img_93, img_94, img_95, img_96 FROM posts WHERE id LIKE "{id}" LIMIT 1')
            res = cur.fetchone()
            cur.close()  # Close the cursor after the query

            if res:
                return res
            
        except sqlite3.Error as e:
            print("Errors get post from db"+str(e))

        return (False, False)

    def getPostCount(self):
        try:
            cur = self.__db.cursor()  # Create a new cursor for fetching
            cur.execute("SELECT COUNT(*) as count FROM posts")
            res = cur.fetchone()
            cur.close()  # Close the cursor after the query

            if res:
                return res['count']
        except sqlite3.Error as e:
            print('Errors getting post count from db: '+str(e))
        return 0

    def catPost(self, cat, limit=5, offset=0):
        """Fetch posts from a specific category with pagination support."""
        try:
            cur = self.__db.cursor()  # Create a new cursor for fetching
            cur.execute(f"SELECT id, title, img, cat, time, tm, \
                               title_0, text_00, text_01, text_02, text_03, text_04, text_05, text_06, text_07, text_08, text_09, img_01, img_02, img_03, img_04, img_05, img_06, \
                               title_1, text_10, text_11, text_12, text_13, text_14, text_15, text_16, text_17, text_18, text_19, img_11, img_12, img_13, img_14, img_15, img_16, \
                               title_2, text_20, text_21, text_22, text_23, text_24, text_25, text_26, text_27, text_28, text_29, img_21, img_22, img_23, img_24, img_25, img_26, \
                               title_3, text_30, text_31, text_32, text_33, text_34, text_35, text_36, text_37, text_38, text_39, img_31, img_32, img_33, img_34, img_35, img_36, \
                               title_4, text_40, text_41, text_42, text_43, text_44, text_45, text_46, text_47, text_48, text_49, img_41, img_42, img_43, img_44, img_45, img_46, \
                               title_5, text_50, text_51, text_52, text_53, text_54, text_55, text_56, text_57, text_58, text_59, img_51, img_52, img_53, img_54, img_55, img_56, \
                               title_6, text_60, text_61, text_62, text_63, text_64, text_65, text_66, text_67, text_68, text_69, img_61, img_62, img_63, img_64, img_65, img_66, \
                               title_7, text_70, text_71, text_72, text_73, text_74, text_75, text_76, text_77, text_78, text_79, img_71, img_72, img_73, img_74, img_75, img_76, \
                               title_8, text_80, text_81, text_82, text_83, text_84, text_85, text_86, text_87, text_88, text_89, img_81, img_82, img_83, img_84, img_85, img_86, \
                               title_9, text_90, text_91, text_92, text_93, text_94, text_95, text_96, text_97, text_98, text_99, img_91, img_92, img_93, img_94, img_95, img_96 FROM posts WHERE cat LIKE '{cat}' ORDER BY tm DESC LIMIT {limit} OFFSET {offset}")
            res = cur.fetchall()
            cur.close()  # Close the cursor after the query

            if res: 
                return res
        except sqlite3.Error as e:
            print('Errors getting post from bd '+str(e))
        return []
    
    def getCategoryPostCount(self, cat):
        """Get the total number of posts for a specific category."""
        try:
            cur = self.__db.cursor()  # Create a new cursor for fetching
            cur.execute(f"SELECT COUNT(*) as count FROM posts WHERE cat LIKE '{cat}'")
            res = cur.fetchone()
            cur.close()  # Close the cursor after the query
            if res:
                return res['count']
        except sqlite3.Error as e:
            print('Errors getting category post count from db: '+str(e))
        return 0

    def changePost(self, id, title, img, cat, *post_data):
        try:
            # Prepare the SQL UPDATE statement
            query = '''UPDATE posts 
                    SET title=?, img=?, cat=?, 
                        title_0=?, text_00=?, text_01=?, text_02=?, text_03=?, text_04=?, text_05=?, text_06=?, text_07=?, text_08=?, text_09=?, 
                        img_01=?, img_02=?, img_03=?, img_04=?, img_05=?, img_06=?, 
                        title_1=?, text_10=?, text_11=?, text_12=?, text_13=?, text_14=?, text_15=?, text_16=?, text_17=?, text_18=?, text_19=?, 
                        img_11=?, img_12=?, img_13=?, img_14=?, img_15=?, img_16=?, 
                        title_2=?, text_20=?, text_21=?, text_22=?, text_23=?, text_24=?, text_25=?, text_26=?, text_27=?, text_28=?, text_29=?, 
                        img_21=?, img_22=?, img_23=?, img_24=?, img_25=?, img_26=?, 
                        title_3=?, text_30=?, text_31=?, text_32=?, text_33=?, text_34=?, text_35=?, text_36=?, text_37=?, text_38=?, text_39=?, 
                        img_31=?, img_32=?, img_33=?, img_34=?, img_35=?, img_36=?, 
                        title_4=?, text_40=?, text_41=?, text_42=?, text_43=?, text_44=?, text_45=?, text_46=?, text_47=?, text_48=?, text_49=?, 
                        img_41=?, img_42=?, img_43=?, img_44=?, img_45=?, img_46=?, 
                        title_5=?, text_50=?, text_51=?, text_52=?, text_53=?, text_54=?, text_55=?, text_56=?, text_57=?, text_58=?, text_59=?, 
                        img_51=?, img_52=?, img_53=?, img_54=?, img_55=?, img_56=?, 
                        title_6=?, text_60=?, text_61=?, text_62=?, text_63=?, text_64=?, text_65=?, text_66=?, text_67=?, text_68=?, text_69=?, 
                        img_61=?, img_62=?, img_63=?, img_64=?, img_65=?, img_66=?, 
                        title_7=?, text_70=?, text_71=?, text_72=?, text_73=?, text_74=?, text_75=?, text_76=?, text_77=?, text_78=?, text_79=?, 
                        img_71=?, img_72=?, img_73=?, img_74=?, img_75=?, img_76=?, 
                        title_8=?, text_80=?, text_81=?, text_82=?, text_83=?, text_84=?, text_85=?, text_86=?, text_87=?, text_88=?, text_89=?, 
                        img_81=?, img_82=?, img_83=?, img_84=?, img_85=?, img_86=?, 
                        title_9=?, text_90=?, text_91=?, text_92=?, text_93=?, text_94=?, text_95=?, text_96=?, text_97=?, text_98=?, text_99=?, 
                        img_91=?, img_92=?, img_93=?, img_94=?, img_95=?, img_96=? 
                    WHERE id = ?'''

            # Collect parameters
            params = (title, img, cat) + post_data + (id,)
            
            # Execute the query
            cur = self.__db.cursor()  # Create a new cursor for fetching
            cur.execute(query, params)
            self.__db.commit()
            cur.close()  # Close the cursor after the query

            return True

        except sqlite3.Error as e:
            print(f'Error updating post in the database with ID {id}: {str(e)}')
            return False

    def deletePost(self, id):
        try:
            cur = self.__db.cursor()  # Create a new cursor for executing queries
            cur.execute("DELETE FROM posts WHERE id = ?", (id,))  # Parameterized query to prevent SQL injection
            self.__db.commit()  # Commit the transaction to save the changes
            cur.close()  # Close the cursor after the query

            return True

        except sqlite3.Error as e:
            print('Error deleting post from db: ' + str(e))
            return False




    





