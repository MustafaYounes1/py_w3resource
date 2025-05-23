"""

Write a Python program to create a HTML calendar with data for a specific year and month.
    Hint: sue the calendar module

<table border="0" cellpadding="0" cellspacing="0" class="month">
<tr><th colspan="7" class="month">February 2025</th></tr>
<tr><th class="sun">Sun</th><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th></tr>
<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="sat">1</td></tr>
<tr><td class="sun">2</td><td class="mon">3</td><td class="tue">4</td><td class="wed">5</td><td class="thu">6</td><td class="fri">7</td><td class="sat">8</td></tr>
<tr><td class="sun">9</td><td class="mon">10</td><td class="tue">11</td><td class="wed">12</td><td class="thu">13</td><td class="fri">14</td><td class="sat">15</td></tr>
<tr><td class="sun">16</td><td class="mon">17</td><td class="tue">18</td><td class="wed">19</td><td class="thu">20</td><td class="fri">21</td><td class="sat">22</td></tr>
<tr><td class="sun">23</td><td class="mon">24</td><td class="tue">25</td><td class="wed">26</td><td class="thu">27</td><td class="fri">28</td><td class="noday">&nbsp;</td></tr>
</table>


"""

import calendar


def main():
    c = calendar.HTMLCalendar(firstweekday=6)
    print(c.formatmonth(2025, 2))


if __name__ == "__main__":
    main()
