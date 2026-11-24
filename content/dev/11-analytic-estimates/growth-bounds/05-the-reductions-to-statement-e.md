---
title: The reductions to Statement E
decls:
  - Formalism.MainNotions.TestSideCounting.stmtE_of_OpNS
  - Formalism.MainNotions.TestSideCounting.stmtE_of_TenNS
  - Formalism.MainNotions.TestSideWords.stmtE_of_TenMP
  - Formalism.MainNotions.TestSideWords.stmtE_of_MP
  - Formalism.MainNotions.Proposition5Numerics.stmtE_of_mem
  - Formalism.MainNotions.PairMembershipBlocks.opSteps_of
  - Formalism.MainNotions.PairMembershipBlocks.restMEM_of_last
  - Formalism.MainNotions.PairMembershipBlocks.stmtE_of_last
  - Formalism.MainNotions.PairMembershipBlocks.stmtE_of_pl
  - Formalism.MainNotions.PairMembershipBlocks.stmtE_of_chain
  - Formalism.MainNotions.TraceSpectra.stmtE
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The reductions to Statement E

This section proves Statement E for every admissible datum. [The closed second theorem](/entry/theorem-ii-closed-of-test-bound/) of Section 3 leaves one input open, the test bound. We reduce the test bound in four stages: to a tensor operator identity and Proposition 5 without its membership hypothesis; then, with [Proposition 5.4.11](/entry/proposition5-holds/) of Section 4, to the membership condition; then to a single step for operators on norm variables and a valuation property of plane coefficients; and last to one valuation bound along chains. The final theorem, [Statement E](/entry/stmt-e/), is used by [the proof of the local bound](/entry/loc-proved/) in Volume 15.

*Statement E in closed form for a datum $\mathcal{D}$* means: for all constants $C_{La}$, $C_k$, $C_{rk}$, $C_{\deg}$, if $\mathcal{D}$ is admissible with these constants, then Statement E holds for $\mathcal{D}$ in the sense of Section 3.

### Tensor operators and the test side

Let $K$ be a field of characteristic $0$, $m \geq 1$ and $n' \geq 1$. For each $t < n'$ let $\nu_t$ be a dominant weight of $\mathrm{GL}_{m+1}$, and let $\mathbb{V}_\nu$ be the tensor product over $t$ of the dual Weyl modules of highest weight $\nu_t$, as in Section 3. For a letter $z = (t, (a, b))$ there is an operator on polynomials in the entries of the matrices $X_t$, and for a list $l$ of letters, $\omega_l$ is the composite of these operators. Let $\Theta$ be the theta map from $\mathrm{Pol}_K(m+1, d)$ to polynomials in the matrix entries, for a choice of signs $\varepsilon : \{0, \dots, n'-1\} \to \{\pm\}$, and let $\langle\ ,\ \rangle$ be the Fock pairing.

**Definition 5.5.1 (Tensor operator property).** The *tensor operator property* says: let $T$ be a set of indices, $c \geq 0$, and let the weights satisfy $\nu_t(0) \leq c$ for $t \in T$ and $\nu_t = 0$ for $t \notin T$. Let $\beta, s \in \mathbb{V}_\nu$. Then there are words $l$ in the letters of $T$, each using each letter at most $c$ times, and scalars $a_l$, such that for every $G \in \mathrm{Pol}_K(m+1, d)$ the polynomial $G' = \sum_l a_l\omega_lG$ lies in $\mathrm{Pol}_K(m+1, d)$ and
$$\langle \Theta(G)\,s, \Theta(H)\,\beta\rangle = \langle \Theta(G'), \Theta(H)\rangle \quad \text{for all } H \in \mathrm{Pol}_K(m+1, d).$$

So multiplication by $s$ on one side and by $\beta$ on the other is the adjoint of a short word in the operators. This is why the operator closure $\mathrm{Op}_{c_0}$ of Section 4 appears.

**Definition 5.5.2 (Test-side steps).** For a datum $\mathcal{D}$ and constants, the *operator step* is a step family in the sense of Section 3: if $\mathcal{D}$ is admissible, then there is $C_1 > 0$ such that a test-side operator statement holds at every level $C \geq C_1$. The *pairing step with constants $(C_H, C_E, C_6, C_{18})$* is the statement: if $\mathcal{D}$ is admissible, then there are $C_D, C_1 > 0$ such that, at every level $C \geq C_1$, Proposition 5 at level $C$ holds with the membership hypothesis on $G$ removed.

**Theorem 5.5.3 (Statement E from the operator and pairing steps).** Let $\mathcal{D}$ be a datum. Assume that for all constants $C_{La}$, $C_k$, $C_{rk}$, $C_{\deg}$ the operator step and the pairing step with $(26, 2, 24, 60)$ hold for $\mathcal{D}$. Then Statement E in closed form holds for $\mathcal{D}$.

Lean: `Formalism.MainNotions.TestSideCounting.stmtE_of_OpNS`.

*Proof.* Let $C \geq 1$ be the constant of the [closed second theorem](/entry/theorem-ii-closed-of-test-bound/), and let $\mathcal{D}$ be admissible with some constants. We must give the test bound with source constants $(C, C + 1, C)$ and plane Gram constants $(26, 2, 24, 60)$. The test bound is the combination of two halves. The first half is a cloud bound on the side of the operators, and it follows from the operator step. The second half is a flatness statement. It follows from a statement $\Xi$ on the test side, and $\Xi$ follows from the pairing step. Now the closed second theorem gives Statement E. $\square$

**Corollary 5.5.4.** Assume the tensor operator property, and let $\mathcal{D}$ be a datum for which the pairing step with $(26, 2, 24, 60)$ holds for all constants. Then Statement E in closed form holds for $\mathcal{D}$.

Lean: `Formalism.MainNotions.TestSideCounting.stmtE_of_TenNS`.

*Proof.* The tensor operator property gives the operator step for every datum and all constants. This is the [Theorem 5.5.3](/entry/stmt-e-of-op-ns/) applied to it. $\square$

### The membership condition

Fix data of the second kind (Section 4). A test polynomial $G$ satisfies the *membership condition* if, for all signed chain data $\mathcal{D}_t$ with degrees $d_{\mathrm{Pl}}$, $d_{\mathrm{No}}$ and shifts $k$ in the tied position, every digit pattern $\rho$, every projector $e$ onto the levels $k$ of the norm variables and every plane index $\nu$, the plane coefficient of index $\nu$ of $e$ applied to the levelled image of $G$ is admissible input for $\mathcal{D}_t$. The *membership step* for a datum says: if $\mathcal{D}$ is admissible, then there is $C_1 > 0$ such that, at every level $C \geq C_1$, every $G$ in the operator closure $\mathrm{Op}_{c_0}$ of the span of the $\mathrm{sym}(B_i)$ satisfies the membership condition.

The membership step and Proposition 5 at level $C$ give the pairing step at level $C$: Proposition 5 assumes the membership condition, and the membership step supplies it for all $G$ in the operator closure.

**Corollary 5.5.5.** Assume the tensor operator property. Let $\mathcal{D}$ be a datum such that, for all constants, the membership step holds and Proposition 5 holds with $(26, 2, 24, 60)$. Then Statement E in closed form holds for $\mathcal{D}$. The tensor operator property holds, so the same conclusion holds without that assumption.

Lean: `Formalism.MainNotions.TestSideWords.stmtE_of_TenMP` (also `Formalism.MainNotions.TestSideWords.stmtE_of_MP`, the form without the tensor operator assumption).

*Proof.* For each choice of constants, the membership step and Proposition 5 give the pairing step, with the larger of the two thresholds. Then the [Corollary 5.5.4](/entry/stmt-e-of-ten-ns/) applies. For the second form, the tensor operator property is [a theorem](/entry/tensor-operators-holds/). $\square$

**Corollary 5.5.6.** Let $\mathcal{D}$ be a datum for which the membership step holds for all constants. Then Statement E in closed form holds for $\mathcal{D}$.

Lean: `Formalism.MainNotions.Proposition5Numerics.stmtE_of_mem`.

*Proof.* This is the previous [Corollary 5.5.5](/entry/stmt-e-of-mp/) applied to [Proposition 5.4.11](/entry/proposition5-holds/), which holds for every datum and all constants. $\square$

### One operator on the norm variables

The membership condition is proved one operator at a time. Let $\mathcal{O}$ be a uniformized ring in the Hida setting with fraction field of characteristic $0$, and let $\mathcal{D}_t$ be signed chain data. The norm variables are $Y_{x,b}$ for letters $x$ and $b < K$. A *$J$-projector for shifts $k$* is a projector $e$ on polynomials in the norm variables onto the levels $k$ of a norm filtration. We write $\mathrm{pc}_\nu(G)$ for the plane coefficient of index $\nu$ of a polynomial $G$ with coefficients in the norm polynomials.

**Definition 5.5.7 (One-operator step).** The *one-operator step* says: let $x_0$ be a letter, $b < K$, and let $\tau$ be one of $\partial/\partial Y_{x_0,b}$, multiplication by $Y_{x_0,b}$, or their product $Y_{x_0,b}\,\partial/\partial Y_{x_0,b}$. Let $e$ be a $J$-projector for shifts $k'$. Assume that for every shift $k$ with $k'_{j,u,0} \leq k_{j,u,0} + [x_0 \in N(j,u)]$ and every $J$-projector $e_1$ for $k$, all plane coefficients $\mathrm{pc}_\nu(e_1G)$ satisfy the admissible input condition with thresholds $(\theta, \vartheta)$ and degree $d$. Then all plane coefficients $\mathrm{pc}_\nu(e\tau G)$ satisfy the same condition.

So one operator on the norm variables costs at most one level of the norm filtration at the letters of $N(j, u)$ that contain $x_0$.

**Lemma 5.5.8 (Operator steps).** The one-operator step implies the list of ten operator steps: transfers of derivatives and of multiplications to the plane and to the norm variables, derivative, Euler and multiplication steps on the plane variables, the one-operator step itself, and two geometric facts on frames (each top index has exactly one letter, and a touching condition).

Lean: `Formalism.MainNotions.PairMembershipBlocks.opSteps_of`.

*Proof.* Nine of the ten steps hold, and the remaining one is the one-operator step. $\square$

**Definition 5.5.9 (Plane coefficient property).** The *plane coefficient property* says: let $\mathcal{O}$ have fraction field of characteristic $0$, let the frames be valid, $n'$ even, and $\mathcal{D}_t$ signed chain data tied to the frames with $J \geq 2$. Let $A_i$ be integral polynomials in the letters of segment $i$, $l$ a label and $\gamma$ an even plane exponent. Assume that the torus valuations of $A$ on the initial letter sets of each segment are at least $t_{j,u}$. Then for every degree $d_{\mathrm{Pl}}$ the plane polynomial built from $(A, l, \gamma)$ in degree $d_{\mathrm{Pl}}$ satisfies:

1. (*chain half*) for every digit pattern and every chain, the digit part has torus valuation at least $t_{j,i}$ on the chain;
2. (*link half*) for $m + 2 \leq r$, the torus valuation on $T(j, m)$ is at least $t_{j, n_L(j) + r - 1 - m}$ minus a degree term.

The conditions on $\mathcal{D}_t$ and $A$ are the same in both halves. Only the chain half is a new input: the link half follows from three facts on degrees and letters of linked segments.

**Proposition 5.5.10 (Membership from the last inputs).** Assume the one-operator step, the plane coefficient property, and an arithmetic step at all levels $C \geq C_1$ for some $C_1 > 0$. Then the membership step holds for every datum and all constants.

Lean: `Formalism.MainNotions.PairMembershipBlocks.restMEM_of_last`.

*Proof.* The membership condition for $G$ in the operator closure follows from two statements. The first is a monomial form of a Lemma 5a: the membership condition for the monomial images $\mathrm{sym}(B_i)$. It follows from a cut statement, built from a table fact, a norm fact for $\mathcal{D}$, a threshold fact, the plane coefficient property, a shift property of admissible input under multiplication by one variable, and the arithmetic step. The second is a word statement: the membership condition is kept when one applies a word of length at most $c_0$ in each letter. It follows from a comparison lemma, a bound on words, and a one-operator statement, and the one-operator statement follows from the ten [operator steps](/entry/op-steps-of/). $\square$

**Corollary 5.5.11.** For a datum $\mathcal{D}$, Statement E in closed form follows from the one-operator step, the plane coefficient property and the arithmetic step. It follows from the plane coefficient property alone. It follows from the chain half of the plane coefficient property alone.

Lean: `Formalism.MainNotions.PairMembershipBlocks.stmtE_of_last` (also `Formalism.MainNotions.PairMembershipBlocks.stmtE_of_pl`, the second form, and `Formalism.MainNotions.PairMembershipBlocks.stmtE_of_chain`, the third form).

*Proof.* The first form is [the Proposition](/entry/rest-mem-of-last/) followed by the [Corollary 5.5.6](/entry/stmt-e-of-mem/). For the second form, the one-operator step holds, and the arithmetic step holds at every level $C \geq 1$ by an arithmetic lemma. For the third form, the link half holds, by the facts on degrees and letters of linked segments. $\square$

### Statement E

**Theorem 5.5.12 (Statement E).** For every datum $\mathcal{D}$, Statement E holds in closed form: if $\mathcal{D}$ is admissible with some constants, then there is $C_0 > 0$ such that Statement E holds with every constant $C \geq C_0$.

Lean: `Formalism.MainNotions.TraceSpectra.stmtE`.

*Proof.* The chain half of the plane coefficient property follows from seven valuation facts: a valuation bound for the evaluation of polynomials, a bound for filtrations, a non-negativity fact, the compatibility of the substitution $\phi$ with monomials and with composition, and two facts on digit parts of $\phi$. Then the third form of the [Corollary 5.5.11](/entry/stmt-e-of-chain/) gives Statement E. $\square$

**Remark 5.5.13 (Formalization).** The pairing step is `RestNS` (DualFockLinear/RestXiPOfNS.lean:70), whose steps `NSStep` are Proposition 5 at level $C$ without `MemAt`; `nsStep_of` adds the membership step (TwistedSubstitution/Proposition5Gram.lean). In the first theorem the hypothesis is asked for all constants, but only the constants of the call are used (DualFockLinear.lean:14); `TestSideCounting.stmtE_of_rests` (DualFockLinear/Closed.lean:49) repeats the same argument. The one-operator step `NoOpStep` quantifies over a datum `D` that does not occur in its body (PlaneCoefficients/NoOpStep.lean:92). The operator step `TSOpStep`, the halves `restCloudB_of_op`, `restFlat_of_Xi`, `restXi_of_NS`, the theta map `Th0`, the operators `opWord`, the norm filtration `normE`, `IsJProj`, `planeCoeff`, the cut statement `rest5aMono_of_cut` and its inputs, `restWord_of`, the nine operator steps, the link facts `linkL`, `lkDeg`, `lkVars`, the arithmetic lemma `arithCondition_of_one_le`, and the seven valuation facts of the last proof (`valAeval`, `valFilt`, `valNN`, `phMon`, `compPh`, `fdigPh`, `fdigSum`) were not unfolded. Since Statement E does not depend on $\mathcal{D}$, the theorem gives one statement for all admissible data.
