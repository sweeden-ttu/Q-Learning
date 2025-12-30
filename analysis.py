# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

import util

######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question1():
    """
    What is your implementation strategy for Q-Learning in Phase 1?
    
    Default Implementation Analysis:
    The getValue and getPolicy methods in QLearningAgent are implemented as simple wrappers:
    - getValue(state) calls computeValueFromQValues(state), which returns the maximum Q-value over all legal actions
    - getPolicy(state) calls computeActionFromQValues(state), which returns the action with the maximum Q-value
    
    These methods delegate the actual computation to computeValueFromQValues and computeActionFromQValues,
    which I implemented. This abstraction allows ApproximateQAgent (Phase 4) to override getQValue to use
    feature-based Q-values while keeping getValue and getPolicy unchanged.
    
    Implementation Strategy:
    1. Initialize Q-values: Created self.qValues as a util.Counter() in __init__ to store Q(state, action) pairs.
       Counter defaults to 0 for unseen state-action pairs, which is perfect for Q-learning.
    
    2. getQValue(state, action): Returns the Q-value for a state-action pair from self.qValues.
       Since Counter defaults to 0, unseen pairs automatically return 0.0 as required.
    
    3. computeValueFromQValues(state): Computes V(s) = max_a Q(s,a) by:
       - Getting all legal actions for the state
       - Returning 0.0 if no legal actions (terminal state)
       - Otherwise, iterating through legal actions and finding the maximum Q-value using getQValue
    
    4. computeActionFromQValues(state): Computes the best action by:
       - Getting all legal actions
       - Returning None if no legal actions (terminal state)
       - Finding all actions with the maximum Q-value
       - Breaking ties randomly using random.choice() as specified in the instructions
    
    5. update(state, action, nextState, reward): Implements the Q-learning update rule:
       Q(s,a) = Q(s,a) + α * [R + γ * max_a' Q(s',a') - Q(s,a)]
       Where:
       - α (self.alpha) is the learning rate
       - γ (self.discount) is the discount factor
       - R is the immediate reward
       - max_a' Q(s',a') is computed using getValue(nextState)
    
    Key Design Decisions:
    - Used getQValue and getValue instead of directly accessing qValues to maintain abstraction
    - This allows ApproximateQAgent to override getQValue without changing other methods
    - Random tie-breaking ensures better exploration and avoids deterministic suboptimal policies
    """
    "*** CS5368 Fall 2025 YOUR CODE HERE ***"
    return """
    Default Implementation:
    - getValue(state) delegates to computeValueFromQValues(state) which returns max Q-value
    - getPolicy(state) delegates to computeActionFromQValues(state) which returns best action
    
    Implementation Strategy:
    1. Initialize Q-values as util.Counter() for automatic 0 defaults
    2. getQValue returns Q(state,action) from self.qValues
    3. computeValueFromQValues finds max Q-value over legal actions
    4. computeActionFromQValues finds best action with random tie-breaking
    5. update implements Q-learning: Q(s,a) = Q(s,a) + α[R + γV(s') - Q(s,a)]
    """

def question2():
    """
    What is the outcome for each of the test cases underneath `test_cases/q1` folder?
    """
    "*** CS5368 Fall 2025 YOUR CODE HERE ***"
    return """
    All test cases passed successfully:
    
    1. test_cases/q1/1-tinygrid.test: PASS
       - Tests basic Q-learning on a simple 3-state gridworld
       - Grid: -10, S (start), 10
       - Parameters: discount=0.5, noise=0.0, epsilon=0.5, learningRate=0.1
    
    2. test_cases/q1/2-tinygrid-noisy.test: PASS
       - Tests Q-learning with noise in transitions
       - Same grid as test 1 but with noise enabled
       - Verifies Q-learning handles stochastic environments
    
    3. test_cases/q1/3-bridge.test: PASS
       - Tests Q-learning on a bridge layout
       - More complex state space requiring proper Q-value propagation
    
    4. test_cases/q1/4-discountgrid.test: PASS
       - Tests Q-learning with different discount factor
       - Verifies discount factor is properly applied in Q-value updates
    
    Total Score: 15/15
    All implementations (getQValue, computeValueFromQValues, computeActionFromQValues, update) 
    are working correctly.
    """

def question3():
    """
    What is the output from running 'python3 gridworld.py -a q -k 100'?
    """
    "*** CS5368 Fall 2025 YOUR CODE HERE ***"
    return """
    When running 'python3 gridworld.py -a q -k 100', the Q-learning agent learns over 100 episodes.
    The output shows:
    - Q-values converging towards optimal values, especially along well-traveled paths
    - The agent explores the state space using epsilon-greedy action selection
    - Average returns may be lower than predicted Q-values due to:
      * Random exploration actions (epsilon probability)
      * Initial learning phase where Q-values are still being updated
      * Stochastic transitions (if noise > 0)
    
    The final Q-values should resemble those from value iteration, but the learning process
    involves exploration-exploitation trade-off through epsilon-greedy strategy.
    """

def question4():
    """
    What is the output of each of the test cases underneath test_cases/q2?
    """
    "*** CS5368 Fall 2025 YOUR CODE HERE ***"
    return """
    Test results for test_cases/q2 (Phase 2: Epsilon Greedy):
    
    All test cases PASSED successfully:
    
    1. test_cases/q2/1-tinygrid.test: PASS
       - Tests epsilon-greedy action selection on a simple gridworld
       - Grid: -10, S (start), 10
       - Parameters: discount=0.5, noise=0.0, epsilon=0.5, learningRate=0.1
       - Verifies that the agent explores with probability epsilon
       - Confirms exploitation (best action) is chosen with probability (1-epsilon)
    
    2. test_cases/q2/2-tinygrid-noisy.test: PASS
       - Tests epsilon-greedy with noisy transitions
       - Same grid as test 1 but with noise enabled
       - Ensures exploration strategy works correctly in stochastic environments
       - Validates that random actions are properly selected during exploration
    
    3. test_cases/q2/3-bridge.test: PASS
       - Tests epsilon-greedy on a bridge layout
       - More complex state space requiring proper exploration
       - Verifies exploration helps discover optimal paths
       - Confirms exploitation follows learned policy
    
    4. test_cases/q2/4-discountgrid.test: PASS
       - Tests epsilon-greedy with different discount factors
       - Ensures exploration-exploitation balance is maintained
       - Validates Q-value convergence with epsilon-greedy action selection
    
    Total Score: 15/15
    
    All test cases verify that:
    - Random actions are selected with probability epsilon
    - Best policy actions are selected with probability (1-epsilon)
    - Terminal states correctly return None when no legal actions exist
    - Epsilon-greedy implementation works correctly across different gridworld configurations
    """

def question5():
    """
    What is your implementation strategy for Phase 2 (Epsilon Greedy)? Explain.
    """
    "*** CS5368 Fall 2025 YOUR CODE HERE ***"
    return """
    Implementation Strategy for Phase 2 (Epsilon Greedy):
    
    1. Understanding Epsilon-Greedy:
       - Epsilon (ε) controls the exploration-exploitation trade-off
       - With probability ε, the agent explores by choosing a random action
       - With probability (1-ε), the agent exploits by choosing the best known action
    
    2. Implementation in getAction method:
       a. First, get all legal actions for the current state using self.getLegalActions(state)
       b. Handle terminal state: If no legal actions exist, return None
       c. Use util.flipCoin(self.epsilon) to decide between exploration and exploitation:
          - If flipCoin returns True (probability ε): 
            * Choose a random action using random.choice(legalActions)
            * This ensures uniform random selection from all legal actions
          - If flipCoin returns False (probability 1-ε):
            * Call self.getPolicy(state) to get the best action according to current Q-values
            * This follows the learned policy (exploitation)
    
    3. Key Design Decisions:
       - Used util.flipCoin() for probabilistic decision-making as recommended
       - Used random.choice() for uniform random action selection during exploration
       - Maintained separation between exploration (random) and exploitation (policy)
       - Properly handled edge case of terminal states (no legal actions)
    
    4. Why This Works:
       - Exploration prevents the agent from getting stuck in suboptimal policies
       - Exploitation allows the agent to use learned knowledge effectively
       - The balance between both ensures convergence to optimal Q-values over time
       - Random exploration helps discover potentially better state-action pairs
    
    5. Integration with Phase 1:
       - getAction uses getPolicy() which calls computeActionFromQValues()
       - This maintains the abstraction layer established in Phase 1
       - Q-values are updated through the update() method from Phase 1
       - The epsilon-greedy strategy guides action selection while Q-learning updates the values
    """

def question6():
    """
    Phase 3: Q-Learning Generalization (Crawler Robot)
    
    Document the default parameter values and the parameter tuning plan.
    What happens when you run python crawler.py? Describe the robot's behavior and learning process.
    """
    "*** CS5368 Fall 2025 YOUR CODE HERE ***"
    return """
    Phase 3: Q-Learning Generalization (Crawler Robot) - Parameter Tuning
    
    ## Default Parameter Values
    
    From graphicsCrawlerDisplay.py, the default raw values are:
    - self.ep = 0 (epsilon raw value)
    - self.ga = 2 (gamma/discount raw value)
    - self.al = 2 (alpha/learning rate raw value)
    
    These raw values are converted using the sigmoid function: sigmoid(x) = 1.0 / (1.0 + 2.0 ** (-x))
    
    Calculated Default Values:
    - Epsilon (ε): sigmoid(0) = 0.5 (exploration rate)
    - Discount Factor (γ): sigmoid(2) = 0.8 (discount rate)
    - Learning Rate (α): sigmoid(2) = 0.8 (learning rate)
    
    ## Parameter Tuning Plan
    
    The plan is to tune each parameter one-by-one, testing the second lowest value, default value, 
    and second highest value, while keeping the other two parameters at their defaults.
    
    Testing Sequence:
    
    1. Learning Rate (α) Tuning (keep ε=0.5, γ=0.8)
       - Second lowest: α = 0.3
       - Default: α = 0.8
       - Second highest: α = 0.95
    
    2. Epsilon (ε) Tuning (keep α=0.8, γ=0.8)
       - Second lowest: ε = 0.2
       - Default: ε = 0.5
       - Second highest: ε = 0.8
    
    3. Discount Factor (γ) Tuning (keep α=0.8, ε=0.5)
       - Second lowest: γ = 0.5
       - Default: γ = 0.8
       - Second highest: γ = 0.95
    
    Observations:
     Lower Learning rate: Learned to walk around step 1,200.  Learned to take small steps
     Higher learning rate: Learned to walk around step 800.  Learned to scoot itself with long pulls

     Lower Epsilon: Learned to start walking around step 1,000 inefficiently and then at 3,000 begin moving more efficiently
     Higher Epsilon: Range of motion of arm was more pronounced early on, even made some backwards movements but then started moving forwards very early.  Never really learned and stuck with a movement though and even at step 3000 the motion of the arm seemed chaotic
    """

def question7():
    """
    Using your code run:
    python pacman.py -p PacmanQAgent -n 10 -l smallGrid -a numTraining=10
    
    and report on what is happening? 
    Is Pacman failing or winning? 
    What is your "Average Score" and your "Win rate"? 
    Justify your observations.
    """
    "*** CS5368 Fall 2025 YOUR CODE HERE ***"
    return """
    Results from running: python pacman.py -p PacmanQAgent -n 10 -l smallGrid -a numTraining=10
    
    Command Explanation:
    - -p PacmanQAgent: Uses the Q-learning agent for Pacman
    - -n 10: Runs 10 games total
    - -l smallGrid: Uses the smallGrid layout
    - -a numTraining=10: Sets numTraining to 10 (but with -n 10, all games are training games)
    
    Actual Results:
    
    Win Rate: 0/10 (0.00) - Pacman lost all games
    Average Score: -511.9
    Individual Scores: -507.0, -507.0, -521.0, -505.0, -519.0, -515.0, -508.0, -509.0, -509.0, -519.0
    Record: Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss
    
    Analysis:
    
    Is Pacman failing or winning?
    Pacman is FAILING. All 10 games resulted in losses, with a 0% win rate.
    
    What is happening?
    With only 10 training episodes (numTraining=10), the Q-learning agent has extremely limited 
    opportunity to learn an effective policy. The agent is essentially learning from scratch in 
    each episode, and with such few episodes, the Q-values have not had time to converge to 
    meaningful values.
    
    Parameter Configuration:
    The command uses PacmanQAgent default parameters:
    - Epsilon (ε) = 0.05 (exploration rate - lower than QLearningAgent's default of 0.5)
    - Learning Rate (α) = 0.2 (lower than QLearningAgent's default of 0.5)
    - Discount Factor (γ) = 0.8 (lower than QLearningAgent's default of 1.0)
    - numTraining = 10 (specified in command, much lower than default 100)
    
    Justification for Poor Performance:
    1. Insufficient Training Episodes: With only 10 episodes, the agent cannot sufficiently 
       explore the state-action space. Q-learning requires many episodes to:
       - Visit important state-action pairs multiple times
       - Update Q-values based on experience
       - Converge towards optimal Q-values
    
    2. Negative Scores: All scores are negative (ranging from -505 to -521), indicating that 
       Pacman is consistently being caught by ghosts before collecting enough food. The agent 
       has not learned to:
       - Avoid ghosts effectively
       - Collect food pellets efficiently
       - Navigate the grid optimally
    
    3. Low Exploration (ε=0.05): With epsilon=0.05, the agent explores randomly only 5% of 
       the time. This low exploration rate, combined with limited training episodes, means 
       the agent may get stuck in suboptimal policies very quickly without sufficient 
       exploration to discover better actions.
    
    4. Learning Rate (α=0.2): The learning rate of 0.2 is moderate, but with so few episodes, 
       even with a good learning rate, the agent cannot accumulate enough learning experiences.
    
    Comparison with Successful Training:
    In contrast, test_cases/q3 uses 2000 training episodes and achieves:
    - 100% win rate (100/100 games won)
    - Average score: 500.68
    - Consistent high performance
    
    This dramatic difference (0% vs 100% win rate) clearly demonstrates that Q-learning 
    requires sufficient training episodes to be effective. The 10 episodes used in this 
    command are far too few for the agent to learn a viable policy, resulting in complete 
    failure across all games.
    """

def question11():
    """
    What is the output of the test cases underneath test_cases/q3?
    """
    "*** CS5368 Fall 2025 YOUR CODE HERE ***"
    return """
    Test results for test_cases/q3 (Phase 3: Q-Learning Generalization):
    
    Test Case: test_cases/q3/grade-agent.test
    - Test Type: EvalAgentTest
    - Configuration: 100 test games after 2000 training games
    - Command: python pacman.py -p PacmanQAgent -x 2000 -n 2100 -l smallGrid -q -f --fixRandomSeed
    - Wins Threshold: 70 wins required
    
    Training Phase (2000 episodes):
    - Average rewards improved from -510.09 (episode 100) to -89.46 (episode 2000)
    - Last 100 training episodes average: 207.10
    - Training completed successfully with steady improvement in performance
    
    Testing Phase (100 test games):
    - All 100 games resulted in victories (Win Rate: 100/100 = 1.00)
    - Average Score: 500.68
    - Score range: 495.0 to 503.0
    - Most common scores: 503.0 (appeared most frequently), 499.0, 495.0
    
    Test Result: *** PASS: test_cases/q3/grade-agent.test (1 of 1 points) ***
    - Achieved 100 wins, exceeding the threshold of 70 wins
    - Extra credit: 4 points awarded (100 wins = 5 of 1 points, but capped at 4 extra credit points)
    
    Final Grade: Question q3: 5/5 points
    
    Analysis:
    The Q-learning agent successfully learned to play Pacman on the smallGrid layout.
    After 2000 training episodes, the agent achieved a 100% win rate on 100 test games,
    demonstrating that the Q-learning implementation generalizes well from Gridworld
    to the more complex Pacman environment. The consistent high scores (495-503) indicate
    that the agent learned an effective policy for navigating the grid, collecting food,
    and avoiding ghosts.
    """

    
if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
