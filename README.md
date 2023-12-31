Title: Dynamic Trader Dashboard App - A Comprehensive Overview

**Introduction:**
- The Dynamic Trader Dashboard App is a web application designed for simulating trading activities.
- This presentation provides an overview of the app, the decision-making process, and the potential areas for further development.

**What I've Built:**
1. **User-Centric Trading Environment:**
   - The app allows 10 unique traders to simulate trading activities.
   - Each trader starts with a balance of $100.

2. **Real-time Trade Simulation:**
   - Traders can simulate trades to either gain a profit or incur losses.
   - Trades are simulated at 1-minute intervals.

3. **Profit/Loss Visualization:**
   - Users have access to a dynamic trade chart that displays real-time profit and loss data.
   - Timestamps are plotted against the balance, providing users with a clear view of their trading performance.

**The Decision-Making Process:**
1. **Technology Stack:**
   - I used Django for the backend to handle user data, while MongoDB was chosen for storing trade data.
   - Plotly was used for data visualization, providing interactive trade charts.

2. **User-Friendly Interface:**
   - The user interface was designed for ease of use, with clear access to trading activities and the trade chart.
   - User interactions were kept straightforward and intuitive.

3. **Data Handling:**
   - User data, including balances and trade histories, were stored in the database.
   - Trade data was continuously recorded, enabling the creation of real-time trade charts.

**Limitations:**
1. **Technical Issues:**
   - Before and during development, I encountered technical issues that significantly impacted my progress. Unfortunately, these issues led to delays and prevented the completion of the admin section, which, in turn, hindered the full implementation of admin functionalities.

    - These challenges represent a critical area that requires attention in future iterations to ensure the app's complete functionality.

**Opportunities for Further Development:**
1. **Admin Dashboard:**
   - Completing the admin dashboard will allow for monitoring and managing user activities.
   - Administrators can track individual traders' performance, detect issues, and manage accounts.

2. **User Authentication:**
   - Implementing user authentication will enhance security and individualize user experiences.
   - Users can have personalized accounts with unique trading histories.

3. **Additional Features:**
   - Implement risk management features, such as setting stop-loss and take-profit levels.
   - Expand trading options and strategies to provide a more realistic trading experience.

**Conclusion:**
- The Dynamic Trader Dashboard App offers a unique platform for users to simulate and visualize trading activities.
- Despite initial challenges, the app provides a strong foundation for further development, including an admin dashboard and additional trading features.
- The future roadmap includes enhancing user authentication, improving data security, and expanding the range of trading options for a richer and more dynamic trading experience.




**App Setup**

1. **Install Python**: Ensure you have Python installed on your system. If not, you can download it from the [Python website](https://www.python.org/downloads/).

2. **Create a Virtual Environment** (Optional but recommended):
   - Open your terminal and navigate to the project's directory.
   - Run the following command to create a virtual environment:
     ```
     python -m venv myenv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       myenv\Scripts\activate
       ```
     - On macOS and Linux:
       ```
       source myenv/bin/activate
       ```

3. **Clone this Repository**: If the app is stored in a repository (e.g., GitHub), clone it to your local machine using Git.

4. **Install Dependencies**: Navigate to the app's root directory and install the required Python packages using `pip`. You can use the `requirements.txt` file
   ```
   pip install -r requirements.txt
   ```

5. **Set Up the Database**:
   - Ensure you have MongoDB installed on your system or you use a server connection.
   - Configure your database connection in the app's(traders)/conn.py settings.

6. **Start the App**:
   - Use the command provided by the app's framework to start the development server. For example, in Django, you can use:
     ```
     python manage.py runserver
     ```

7. **Access the App**:
   - Open a web browser and navigate to the URL provided by the development server (e.g., http://localhost:8000).

8. **Start Simulating Trades**:
    - You can start the simulation as a trader. Ensure you follow the provided steps for trading.

9. **Access the User Dashboard**:
    - As a registered user, you can access your dashboard. Here, you can view your balance and the profit/loss graph.

By following these steps, you can set up and use the app effectively.


**Screenshots**

![Homepage](screenshots/homepage.png)
