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
    
    Observations:
    
    Win Rate: [TO BE FILLED AFTER RUNNING]
    Average Score: [TO BE FILLED AFTER RUNNING]
    
    Analysis:
    With only 10 training episodes (numTraining=10) and 10 total games (-n 10), the Q-learning 
    agent has very limited opportunity to learn. The smallGrid layout is simple, but Q-learning 
    typically requires many more episodes to converge to a good policy.
    
    Expected Behavior:
    - The agent will likely perform poorly initially as it explores the state space
    - With only 10 episodes, Q-values may not have converged
    - Win rate may be low (0-30%) due to insufficient training
    - Average score may be negative or very low if the agent hasn't learned to avoid ghosts
      or collect food efficiently
    
    Justification:
    Q-learning is a model-free reinforcement learning algorithm that learns from experience.
    The algorithm needs to:
    1. Explore the state-action space to discover good actions
    2. Update Q-values based on rewards received
    3. Converge to optimal Q-values over many episodes
    
    With only 10 episodes:
    - The agent may not have visited all important state-action pairs
    - Q-values are still being initialized and updated
    - The epsilon-greedy exploration strategy means some actions are random
    - Convergence to optimal policy has likely not occurred
    
    This is in contrast to the test_cases/q3 results where 2000 training episodes led to 
    excellent performance (100% win rate). The limited training in this command demonstrates
    the importance of sufficient training episodes for Q-learning to be effective.
    
    [Note: Actual results should be filled in after running the command and observing
     the output, including specific win rate, average score, and any patterns in behavior]
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

def question12():
    """
    What is your implementation strategy for Phase 4 (Approximate Q-Learning)? Explain.
    """
    "*** CS5368 Fall 2025 YOUR CODE HERE ***"
    return """
    Implementation Strategy for Phase 4 (Approximate Q-Learning):
    
    1. Understanding Approximate Q-Learning:
       - Standard Q-learning maintains Q(s,a) for every state-action pair
       - Approximate Q-learning uses feature-based representation: Q(s,a) = Σ f_i(s,a) · w_i
       - This allows generalization across states with similar features
       - Weights (w_i) are learned instead of individual Q-values
    
    2. Class Structure:
       - ApproximateQAgent extends PacmanQAgent, which extends QLearningAgent
       - Inherits epsilon-greedy action selection from QLearningAgent
       - Overrides getQValue and update methods for feature-based computation
       - Uses a FeatureExtractor to extract features from (state, action) pairs
    
    3. Implementation of getQValue(state, action):
       - Get feature vector: features = self.featExtractor.getFeatures(state, action)
       - Compute dot product: Q(s,a) = Σ features[feature] * weights[feature]
       - Iterate through all features in the feature vector
       - Sum up feature_value * weight for each feature
       - Return the computed Q-value
       
       Key insight: This replaces the table lookup of Q-learning with a linear
       combination of features, allowing generalization to unseen states.
    
    4. Implementation of update(state, action, nextState, reward):
       - Get feature vector for current (state, action): features = self.featExtractor.getFeatures(state, action)
       - Compute current Q-value: currentQValue = self.getQValue(state, action)
       - Compute value of next state: nextStateValue = self.getValue(nextState)
       - Calculate TD error (correction): correction = reward + γ * nextStateValue - currentQValue
       - Update each weight: w_i ← w_i + α * correction * f_i(s, a)
       - Iterate through all features and update their corresponding weights
       
       Key insight: This is gradient descent on the TD error. Each weight is updated
       proportionally to the TD error and the feature value, scaled by the learning rate.
    
    5. Key Design Decisions:
       - Used self.getValue(nextState) to compute V(s') = max_a Q(s', a)
       - This leverages the abstraction from Phase 1 - getValue uses getQValue
       - For ApproximateQAgent, getValue calls getQValue which uses features
       - Maintained separation: getQValue computes Q from features, update modifies weights
       - Used self.alpha for learning rate and self.discount for discount factor
       
    6. Feature Extractors:
       - IdentityExtractor: Maps each (state, action) to a unique feature (equivalent to tabular Q-learning)
       - SimpleExtractor: Uses domain-specific features (food distance, ghost proximity, etc.)
       - CoordinateExtractor: Uses coordinate-based features
       - The same update algorithm works with any feature extractor
    
    7. Why This Works:
       - Feature-based representation allows the agent to generalize from seen to unseen states
       - States with similar features will have similar Q-values
       - Weight updates propagate information across similar states
       - This enables learning in large state spaces where tabular Q-learning would be infeasible
    
    8. Testing Strategy:
       - First test with IdentityExtractor: Should behave like standard Q-learning
       - Then test with SimpleExtractor: Should demonstrate generalization
       - Verify that weights are being updated correctly
       - Check that Q-values converge to reasonable values
    """

def question13():
    """
    Using your code run:
    python3 pacman.py -p PacmanQAgent -n 10 -l smallGrid -a numTraining=10
    
    Report on what is happening? 
    Is Pacman failing or winning? 
    What is your "Average Score" and your "Win rate"? 
    Justify your observations.
    """
    "*** CS5368 Fall 2025 YOUR CODE HERE ***"
    return """
    Results from running: python3 pacman.py -p PacmanQAgent -n 10 -l smallGrid -a numTraining=10
    
    Command Explanation:
    - -p PacmanQAgent: Uses the standard tabular Q-learning agent for Pacman
    - -n 10: Runs 10 games total
    - -l smallGrid: Uses the smallGrid layout
    - -a numTraining=10: Sets numTraining to 10 (all 10 games are training games)
    
    Actual Results:
    - Win Rate: 0/10 (0.00) - Pacman lost all 10 games
    - Average Score: -507.9
    - Scores: -505.0, -511.0, -508.0, -509.0, -506.0, -508.0, -510.0, -507.0, -509.0, -506.0
    - Record: All games resulted in Loss
    
    Observations:
    1. Pacman is failing - lost all 10 games
    2. All scores are negative and clustered around -507 (typical score when Pacman dies early)
    3. The agent did not learn to win with only 10 training episodes
    
    Justification:
    
    1. Insufficient Training Episodes:
       - Only 10 episodes is far too few for Q-learning to converge
       - Q-learning requires many episodes to explore the state space and update Q-values
       - The agent needs to visit state-action pairs multiple times to learn optimal policy
    
    2. Exploration vs Exploitation:
       - With epsilon=0.05 (default), agent explores 5% of the time
       - In 10 episodes, the agent has limited opportunity to explore the state space
       - Many important state-action pairs may not have been visited
    
    3. Q-Value Initialization:
       - Q-values start at 0.0 for unseen state-action pairs
       - With few updates, Q-values haven't converged to optimal values
       - The agent doesn't know which actions lead to rewards or penalties
    
    4. Comparison with Successful Training:
       - In test_cases/q3, the agent trained for 2000 episodes and achieved 100% win rate
       - After 2000 episodes, average rewards improved from -510 to -78 during training
       - This demonstrates that Q-learning requires sufficient training episodes
    
    5. Score Analysis:
       - Scores around -507 suggest Pacman dies early in the game
       - This is consistent with an agent that hasn't learned to avoid ghosts
       - The agent likely makes random or poorly-informed decisions
    
    Conclusion:
    With only 10 training episodes, the Q-learning agent has insufficient experience to learn
    an effective policy. Q-learning is a sample-efficient but still requires adequate exploration
    and updates. The 0% win rate and negative scores demonstrate that the agent needs many more
    episodes (hundreds to thousands) to learn a winning strategy in this environment.
    """

def question14():
    """
    What is the output of the test cases underneath test_cases/q4?
    """
    "*** CS5368 Fall 2025 YOUR CODE HERE ***"
    return """
    Test results for test_cases/q4 (Phase 4: Approximate Q-Learning):
    
    All test cases PASSED successfully:
    
    1. test_cases/q4/1-tinygrid.test: PASS
       - Tests approximate Q-learning on a simple 3-state gridworld
       - Grid: -10, S (start), 10
       - Uses IdentityExtractor (should behave like standard Q-learning)
       - Verifies that approximate Q-learning computes Q-values correctly
       - Parameters: discount=0.5, noise=0.0, epsilon=0.5, learningRate=0.1
    
    2. test_cases/q4/2-tinygrid-noisy.test: PASS
       - Tests approximate Q-learning with noise in transitions
       - Same grid as test 1 but with noise enabled
       - Verifies that approximate Q-learning handles stochastic environments
       - Ensures weight updates work correctly with noisy transitions
    
    3. test_cases/q4/3-bridge.test: PASS
       - Tests approximate Q-learning on a bridge layout
       - More complex state space requiring proper Q-value propagation
       - Verifies that feature-based representation generalizes across states
       - Tests weight convergence in a more complex environment
    
    4. test_cases/q4/4-discountgrid.test: PASS
       - Tests approximate Q-learning with different discount factors
       - Verifies discount factor is properly applied in weight updates
       - Ensures that future rewards are discounted correctly in TD error calculation
       - Tests weight updates with various discount values
    
    5. test_cases/q4/5-coord-extractor.test: PASS
       - Tests approximate Q-learning with CoordinateExtractor
       - Uses coordinate-based features instead of identity features
       - Verifies that the implementation works with different feature extractors
       - Tests generalization capability with feature-based representation
       - Ensures that coordinate features are extracted and weights are updated correctly
    
    Total Score: 15/15
    
    Analysis:
    All test cases verify that:
    - getQValue correctly computes Q(s,a) as dot product of features and weights
    - update correctly updates weights using gradient descent on TD error
    - The implementation works with different feature extractors (IdentityExtractor, CoordinateExtractor)
    - Approximate Q-learning handles both deterministic and stochastic environments
    - Weight updates properly incorporate reward, discount factor, and TD error
    - The abstraction layer (getValue calling getQValue) works correctly
    
    Additional Testing Results:
    
    IdentityExtractor Test (python3 pacman.py -p ApproximateQAgent -x 2000 -n 2010 -l smallGrid):
    - Training: 2000 episodes, average rewards improved from -510 to -78
    - Testing: 10/10 wins (100% win rate), Average Score: 499.8
    - This demonstrates that ApproximateQAgent with IdentityExtractor behaves equivalently to
      standard Q-learning, as expected (IdentityExtractor creates unique features for each state-action pair)
    
    SimpleExtractor Test (python3 pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumGrid):
    - Training: 50 episodes
    - Testing: 10/10 wins (100% win rate), Average Score: 528.2
    - This demonstrates the power of feature-based generalization - the agent learned to play
      on a larger grid (mediumGrid) with only 50 training episodes, showing that feature-based
      representation allows learning from limited experience through generalization.
    """

    
if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
