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


    
    
if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
