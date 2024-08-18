# Postmortem: The Day the Payment Gateway Decided to Take a Nap 💤

## Issue Summary

**Duration:**  
Picture this: it’s a sunny August morning, and our payment gateway decides to go on a coffee break from 08:30 AM GMT to 10:15 AM GMT. That’s 1 hour and 45 minutes of transaction turmoil.

**Impact:**  
For 70% of our eager shoppers, it was like trying to pay for groceries with Monopoly money—delays, timeouts, and a whole lot of frustration. As for us? We watched a potential $150,000 slip away faster than you can say "payment failed."

**Root Cause:**  
Turns out, our load balancer decided to play favorites, piling all the traffic onto one poor server while the others sat around twiddling their virtual thumbs. The result? One very overworked server and a whole lot of unhappy customers.


## Timeline

- **08:30 AM GMT:** The alarms went off! (Literally. Our monitoring system detected a spike in transaction failures.) 🚨
- **08:35 AM GMT:** Our on-call engineer was rudely awakened (okay, maybe not rudely, but definitely urgently) and got to work. 🛌➡️💻
- **08:40 AM GMT:** First guess: "It’s gotta be the database, right?" (Spoiler: It wasn’t.) 🤔
- **08:50 AM GMT:** Database team says, "All clear here!" and hands it back. 🙅‍♂️
- **09:00 AM GMT:** A customer rings in: "Uh, guys? I’m trying to buy stuff here!" Confirmation that users were indeed facing issues. ☎️
- **09:10 AM GMT:** We escalate to the network team. Someone suggests, "Maybe the load balancer's taking its own load too seriously?" 💡
- **09:20 AM GMT:** Bingo! Load balancer misconfiguration detected. One server’s about to call it quits from overload. 🎯
- **09:30 AM GMT:** Manual traffic redistribution. (Imagine moving traffic cones around a virtual highway.) 🚧
- **09:50 AM GMT:** Things start looking up—transactions are going through like they’re supposed to. 👍
- **10:15 AM GMT:** Full service is restored. The load balancer is back on its best behavior. 🎉

## Root Cause and Resolution

**Root Cause:**  
Our load balancer had a bit of a diva moment. After a recent update, it decided to dump almost all the traffic on one server, leading to a breakdown. The misconfiguration was subtle but deadly—one small parameter set wrong, and suddenly, the whole thing falls apart.

**Resolution:**  
Step one: redistribute the traffic manually (because who needs sleep, right?). Step two: correct the load balancer configuration and test it like our jobs depend on it (because they kinda do). Step three: deploy the fix and breathe a sigh of relief as transactions start flowing smoothly again.

## Corrective and Preventative Measures

**Improvements:**  
- Let’s make sure our load balancers know how to share the load next time. We’re improving the update process so no one gets overloaded (literally).
- Our monitoring system needs a sixth sense—let’s add some metrics to catch these issues before they cause a scene.
- Traffic rebalancing automation: because why do it manually when we can let the machines handle it?

**Tasks:**
1. **Patch Load Balancer Configuration:** Get that load balancer sorted out so it distributes traffic like a pro.
2. **Monitoring Enhancement:** New metrics, more insights—let’s catch the next issue before it catches us.
3. **Automation:** Develop a script to automate traffic redistribution—because we’re all about working smarter, not harder.
4. **Training:** A crash course for the team on avoiding future misconfigurations. (Maybe with some pizza as an incentive? 🍕)

By implementing these measures, we’re setting ourselves up for smoother transactions and fewer surprises. Because in tech, surprises are rarely fun.
