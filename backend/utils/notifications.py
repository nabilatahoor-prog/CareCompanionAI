import streamlit as st
from datetime import datetime, timedelta

class Notifications:
    def __init__(self):
        self.notifications = []
    
    def add_notification(self, user_id, title, message, notification_type='info'):
        notification = {
            'id': len(self.notifications),
            'user_id': user_id,
            'title': title,
            'message': message,
            'type': notification_type,
            'timestamp': datetime.now(),
            'read': False
        }
        self.notifications.append(notification)
        return notification
    
    def get_user_notifications(self, user_id, unread_only=False):
        user_notifs = [n for n in self.notifications if n['user_id'] == user_id]
        if unread_only:
            user_notifs = [n for n in user_notifs if not n['read']]
        return sorted(user_notifs, key=lambda x: x['timestamp'], reverse=True)
    
    def mark_as_read(self, notification_id):
        for n in self.notifications:
            if n['id'] == notification_id:
                n['read'] = True
                return True
        return False
    
    def show_notifications_ui(self, user_id):
        notifs = self.get_user_notifications(user_id, unread_only=True)
        
        if notifs:
            with st.expander(f"🔔 Notifications ({len(notifs)})"):
                for notif in notifs:
                    if notif['type'] == 'warning':
                        st.warning(f"**{notif['title']}**\n{notif['message']}")
                    elif notif['type'] == 'success':
                        st.success(f"**{notif['title']}**\n{notif['message']}")
                    else:
                        st.info(f"**{notif['title']}**\n{notif['message']}")
                    
                    if st.button("Mark as read", key=f"read_{notif['id']}"):
                        self.mark_as_read(notif['id'])
                        st.rerun()

notifications = Notifications()
