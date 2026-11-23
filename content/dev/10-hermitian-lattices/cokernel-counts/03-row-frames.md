---
title: Row frames
decls:
  - Formalism.L2.SG.Pf.RowForm.scalarAgreeC_of_scalT
  - Formalism.L2.SG.Pf.RowForm.commonFrameC_all
  - Formalism.L2.SG.Pf.RowForm.classFrameOO_all
  - Formalism.L2.SG.Pf.RowForm.classFrameC_all
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Row frames

A coefficient of the theta series is a sum over terms $s$, and the terms fall into row classes. Within one row class, each term contributes an operator between two fixed Hermitian spaces. This section shows that all these operators are, up to one phase, conjugates of a single operator by one pair of unitary maps: they share a common frame. From this, the squared norm of the sum over a row class is a constant times the squared norm of a single lifted value. The main result is the Theorem (Norm of a row class). It is used in the [Theorem 3.29](/entry/row-form-c-of-leaves3/) that puts the coefficients of the theta series into row form.

Fix the global datum. For a row class $R$ and a level $\rho$, let $\mathcal{L}(R, \rho)$ be the set of lifted terms of $R$ at level $\rho$. Each term $s$ has a weight $\mathrm{wt}(s) \in \mathbb{C}$, a normalized amplitude $A_N(s)$, a representative point $\mathrm{pt}(s)$, a scalar $c(s)$ and a character value $\chi(s)$ of absolute value $1$. The *lifted vector* of $s$ is $\ell(s) = \mathrm{wt}(s) A_N(s)$, a vector in a finite-dimensional Hermitian space. The *lifted value* $\lambda(R, \rho)$ is the corresponding vector for the class $R$ at its base point. Two positive constants $c_0$ and $c_0'$ come with the frame data.

**Definition 8.3.1 (Scalar agreement).** For a term $s$ and an infinite place $v$, let $n_v(s)$ be the coordinate vector of $s$ at $v$, scaled by the inverse of the leading determinant of the class. We say that the scalars *agree* on $(R, \rho)$ if for all relevant $s_1, s_2 \in \mathcal{L}(R, \rho)$ and every infinite place $v$, $n_v(s_1) = n_v(s_2)$.

**Definition 8.3.2 (Scalar test).** Let $\kappa(s)$ be the class invariant of a term $s$. The *scalar test* holds if for generic terms $s_1, s_2$ in the same row, with nonzero leading coefficient, the following are equivalent: (a) $s_0(s_1, s_2) = 1$ and the scalars of $s_1$ and $s_2$ agree; (b) $\kappa(s_1) = \kappa(s_2)$.

So the scalar test says that the class invariant $\kappa$ detects exactly when two terms have the same scalar data.

**Theorem 8.3.3 (Scalar agreement from the scalar test).** Assume the scalar test. Then the scalars agree on every $(R, \rho)$.

Lean: `Formalism.L2.SG.Pf.RowForm.scalarAgreeC_of_scalT`.

*Proof.* First the scalar test gives a rational form of agreement: the coordinate vectors of two relevant terms agree after projection to the rational orthogonal complement of the frame. Two terms of $\mathcal{L}(R, \rho)$ have the same $\kappa$ by the definition of a row class, so by the test their scalars agree. The coordinates at each infinite place $v$ are the images of these rational vectors under the embedding at $v$, so they agree at every $v$. $\square$

**Definition 8.3.4 (Common frame).** For unitary maps $U, U'$ let $\Phi_{U, U'}(s)$ be the frame value of the term $s$ in the frame $(U, U')$. The terms of a row class have a *common frame* if there are unitary $U, U'$ and $\zeta \in \mathbb{C}$ with $|\zeta| = 1$ such that, for all frames $(A, B)$ and terms $s$ with $\chi(s) \, O(s) = \Phi_{A, B}(s)$, we have $\Phi_{A, B}(s) = \zeta \, \Phi_{U, U'}(s)$. Here $O(s)$ is the operator of $s$.

**Theorem 8.3.5 (Common frame).** Assume the ten standing conditions on the frame data: the hypotheses on the local systems at each place, the theta, unit, determinant, point, frame, value, scalar and volume conditions. Then the terms of each row class have a common frame.

Lean: `Formalism.L2.SG.Pf.RowForm.commonFrameC_all`.

*Proof.* Fix a base term $s_0$ of the row class. The local frame at each place is determined by the local system, and at a place where two terms differ, the scalar condition (from the Theorem (Scalar agreement from the scalar test) in the applications) shows that the two local frames differ by a scalar of absolute value $1$. The product of these scalars over the places is the phase $\zeta$. Take $(U, U')$ to be the frame of $s_0$. $\square$

**Definition 8.3.6 (Class frame).** A row class has a *class frame* if there are unitary $U, U'$ and $\zeta$ with $|\zeta| = 1$ such that for each term $s$ of the class
$$\chi(s) \, O(s) = \zeta \, c(s) \; U \circ A(\mathrm{pt}(s)) \circ U'^{-1},$$
where $A(x)$ is the unscaled operator at the point $x$.

**Theorem 8.3.7 (Class frame).** Under the ten standing conditions and the two additional conditions on values and points, each row class has a class frame.

Lean: `Formalism.L2.SG.Pf.RowForm.classFrameOO_all`.

*Proof.* Each term has a normal form: $\chi(s) O(s)$ equals $c(s)$ times a frame value of $A(\mathrm{pt}(s))$ in some frame $(A_s, B_s)$. This holds by the normal form result for all terms. The [Theorem (Common frame)](/entry/common-frame-c-all/) replaces each frame $(A_s, B_s)$ by the one frame $(U, U')$ at the cost of the phase $\zeta$. $\square$

**Theorem 8.3.8 (Norm of a row class).** Assume the conditions of the Theorem (Class frame), that the volume constant $\mathrm{vol}_2$ is positive and that $c_0 c_0' \geq 0$. Then for each row class $R$ and level $\rho$,
$$\Bigl\| \sum_{s \in \mathcal{L}(R, \rho)} \ell(s) \Bigr\|^2 = (c_0 c_0')^{-1} \, \bigl\| \lambda(R, \rho) \bigr\|^2.$$

Lean: `Formalism.L2.SG.Pf.RowForm.classFrameC_all`.

*Proof.* By the [Theorem (Class frame)](/entry/class-frame-oo-all/), every lifted vector $\ell(s)$ is $\zeta$ times the image under the fixed unitary pair $(U, U')$ of the vector $c(s) \, \mathrm{wt}(s) A(\mathrm{pt}(s))$. Unitary maps and a phase preserve norms, so the norm of the sum is the norm of $\sum_s c(s) \, \mathrm{wt}(s) A(\mathrm{pt}(s))$. This sum is the lifted value at the base point times the normalization $(c_0 c_0')^{-1/2}$. The positivity of the volume makes the normalization defined, and $c_0 c_0' \geq 0$ makes the square root real. $\square$

**Remark 8.3.9 (Formalization).** The three frame results take the same ten hypotheses (named `hAtS`, `hTP`, `hCU`, `hDF`, `hPT`, `hFT`, `hVA`, `hSc`, `hV`, `hAt` in [ClassFrameAll.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/RowFrameCoherence/ClassFrameAll.lean#L121)), and we did not unfold each of them; the list in the Theorem (Common frame) only names them. The proofs are short compositions: the class frame is the normal form result combined with the common frame (line 141), and the norm formula is the class frame combined with the volume and sign conditions (line 154). The scalar agreement passes through a rational form (OrthogonalComplementRational.lean:306) that we did not unfold. The arguments given in the proofs above describe what the cited results provide, not a check of every step of their proofs. The normalization $(c_0 c_0')^{-1}$ is a real inverse, so it is $0$ if $c_0 c_0' = 0$; the condition $c_0 c_0' \geq 0$ allows this case.
