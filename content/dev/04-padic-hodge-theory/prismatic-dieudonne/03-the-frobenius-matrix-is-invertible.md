---
title: The Frobenius matrix is invertible
decls:
  - GlobalTheory.FrobUnit.frob_matrix_isUnit
  - GlobalTheory.T.frobenius_matrix_isUnit_adapted_basis
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Frobenius matrix is invertible

This section introduces the frames over $A_{\inf}$ that the next three sections work in, and it proves that the matrix of the Frobenius in a lifted adapted basis of quasi-logarithms is invertible. The matrix $U$ is defined by the relation $\varphi(e) \equiv e \cdot U \cdot \mathrm{diag}(p, 1)$ modulo integral series, and the theorem says that the factor $p$ on the first block is the only obstruction to invertibility. The theorem on period matrices ([Theorem 5.4.3](/entry/window-matrices/)) uses this to get the condition that $U$ is a unit in its list of relations.

We keep the notation of the first section. Let $O^\flat$ be the tilt of $O$ and $A_{\inf} = W(O^\flat)$, with Fontaine's map $\theta : A_{\inf} \to O$ and the Witt vector Frobenius $\varphi$; see [period rings](/learn/galois-representations/#period-rings). Let $\varepsilon \in O^\flat$. For $n \geq 0$ let $\zeta_n \in O$ be the $n$-th component of $\varepsilon$. We call $\varepsilon$ a *primitive system* if $\zeta_n$ is a primitive $p^n$-th root of unity for each $n$. Put $\mu = [\varepsilon] - 1 \in A_{\inf}$.

**Definition 5.3.1 (Frame over $A_{\inf}$).** Let $\varepsilon \in O^\flat$. A *frame over $A_{\inf}$* for $\varepsilon$ consists of rings $B$ and $Q$ with $Q$ a $B$-algebra, ring maps $a : A_{\inf} \to B$, $\theta_B : B \to O$, $\sigma : B \to B$ and $s : Q \to Q$, and an element $\tau \in B$, such that:

1. $(B, Q, \theta_B)$ is a frame for $p$;
2. $\theta_B(a(x)) = \theta(x)$ and $\sigma(a(x)) = a(\varphi(x))$ for all $x \in A_{\inf}$;
3. $s$ extends $\sigma$ along $B \to Q$, and $p$ divides $\sigma(b) - b^p$ for all $b \in B$;
4. $p \tau = a(\mu)$ and $\tau^2 = 0$;
5. every $b \in B$ has the form $a(x) + \tau a(y)$;
6. $\tau a(y) = 0$ if and only if $\mu$ divides $y$;
7. $\tau$ divides $a(x)$ if and only if $\mu$ divides $x$.

So $B$ is a square zero extension of a quotient of $A_{\inf}$ by an element $\tau$ that stands for $\mu / p$. Condition 6 says that the annihilator of $\tau$ among the elements $a(y)$ is the image of $\mu A_{\inf}$, and condition 7 says that $a(x)$ lies in $\tau B$ exactly when $x$ lies in $\mu A_{\inf}$. We write $\theta$ for $\theta_B$ when no confusion is possible.

For a ring map $s$ of $Q$ and a series $f$ over $Q$ in $d$ variables, let $\varphi_s(f)$ be the series obtained by applying $s$ to the coefficients of $f$ and then putting $X_i^p$ for $X_i$. For $a, b$ in a ring, let $\mathrm{diag}_{d,k}(a, b)$ be the diagonal matrix of size $d + k$ whose first $d$ entries are $a$ and whose last $k$ entries are $b$. For a family $e$ indexed by $\{1, \ldots, d\} \sqcup \{1, \ldots, k\}$ and a vector $b$ over $B$ with the same index set, put $\langle b, e \rangle = \sum_l b_l e_l$.

**Theorem 5.3.2 (The Frobenius matrix is a unit).** Let $p$, $C$, $v$ and $O$ be as in the first section. Let $\varepsilon \in O^\flat$ be a primitive system and let $(B, Q, a, \theta, \sigma, s, \tau)$ be a frame over $A_{\inf}$ for $\varepsilon$. Let $G$ be a $p$-divisible group over $O$ and let $c$ be a chart of $G$ of dimension $d$. Let $\mu'$ be a lift of a law along $\theta$ in dimension $d$ whose image under $\theta$ is the law $\mu_c$ of the chart. Let $k \geq 0$ and let $e$ be a family of series over $Q$ in $d$ variables, indexed by $\{1, \ldots, d\} \sqcup \{1, \ldots, k\}$, that is a basis of quasi-logarithms for $\mu'$ and is adapted for $\theta$ and $\mu'$. Let $U$ be a square matrix over $B$ of size $d + k$, and put $P = U \cdot \mathrm{diag}_{d,k}(p, 1)$. Assume that for each index $i$:

1. the series $\varphi_s(e_i) - \langle P_{\cdot, i}, e \rangle$ is integral;
2. if $i$ is in the first block, the series $\varphi_s(e_i) - \langle P_{\cdot, i}, e \rangle$ has coefficients in $pB$.

Then $U$ is invertible.

Lean: `GlobalTheory.FrobUnit.frob_matrix_isUnit` (also `GlobalTheory.T.frobenius_matrix_isUnit_adapted_basis`, a wrapper).

The proof uses one lemma on frames.

**Lemma 5.3.3.** Let $(B, Q, \theta)$ be a frame for $p$ and $b \in B$. If $\theta(b)$ is a unit of $O$, then $b$ is a unit of $B$.

*Proof.* Since $\theta$ is surjective, choose $b'$ with $\theta(b') = \theta(b)^{-1}$, and put $x = b b' - 1$. Then $\theta(x) = 0$, so $x^p = p y$ for some $y$ by condition 4 of a frame. Since $B$ is $p$-adically complete, $p y$ lies in the Jacobson radical of $B$, so $1 + p y \cdot u$ is a unit for every $u$. The geometric sum gives
$$(1 + x) \sum_{i < p} (-x)^i = 1 - (-x)^p = 1 - (-1)^p p y.$$
The right side is a unit. So $1 + x = b b'$ is a unit, and so is $b$. $\square$

*Proof of the theorem.* The ring $O$ is a valuation ring, so it is local. Let $\mathfrak{m}$ be its maximal ideal and $k_O = O/\mathfrak{m}$ its residue field. Since $p$ is not a unit, $p \in \mathfrak{m}$. For $b \in B$ we have $\sigma(b) = b^p + p z$ for some $z$, so $\theta(\sigma(b)) \equiv \theta(b)^p$ modulo $\mathfrak{m}$. Call a vector $w$ over $B$ *small* if $\theta(w_l) \in \mathfrak{m}$ for every $l$.

1. *Key step.* We claim: if $U \sigma(w)$ is small, then $w$ is small. We take as given two results on Frobenius and quasi-logarithms, under the hypotheses of the theorem. The first says that if $U \sigma(w)$ is small, then the first block of $w$ is small. The second says that if $U \sigma(w')$ is small for the vector $w'$ that is $0$ on the first block and equal to $w$ on the second block, then the second block of $w$ is small. To apply the second, write $U \sigma(w') = U \sigma(w) - U \sigma(w'')$, where $w''$ is $w$ on the first block and $0$ on the second. The first term is small by hypothesis. The second is small, since the first block of $w$ is small and $\theta \circ \sigma$ preserves $\mathfrak{m}$ by the congruence above. So both blocks of $w$ are small.
2. *Reduction to the residue field.* By the lemma it suffices that $\theta(\det U) = \det \theta(U)$ is a unit of $O$. Suppose not. Then the matrix $\bar U$ of residues of $\theta(U)$ over $k_O$ has determinant $0$, so there is a vector $x \neq 0$ over $k_O$ with $\bar U x = 0$.
3. *Taking $p$-th roots.* The field $C$ is algebraically closed, and an element of $C$ whose $p$-th power lies in $O$ lies in $O$. So every element of $O$ has a $p$-th root in $O$. Since $\theta$ and $O \to k_O$ are surjective, choose $w_l \in B$ such that the residue of $\theta(w_l)^p$ is $x_l$, for each $l$.
4. *Conclusion.* By the congruence above, the residue of $\theta(\sigma(w_l))$ is $x_l$. So the residue of $\theta(U \sigma(w))$ is $\bar U x = 0$, and $U \sigma(w)$ is small. By step 1, $w$ is small. Then $x_l$, the residue of $\theta(w_l)^p$, is $0$ for every $l$. This contradicts $x \neq 0$. $\square$

The proof shows a little more: the matrix $U$ is a unit as soon as its reduction to $k_O$ is a unit, and the semilinear map $w \mapsto U \sigma(w)$ is injective on vectors modulo $\mathfrak{m}$. The two results taken as given carry the arithmetic content, since they are where the chart, the basis and the primitive system enter.

**Remark 5.3.4 (Formalization).** The theorem is in [FrobeniusMatrixIsUnitAdaptedBasis.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FrobeniusMatrixIsUnitAdaptedBasis.lean#L40) and the lemma is `isUnit_of_isUnit_map` at line 9 of the same file. The frame over $A_{\inf}$ is `BFrame` in [EqZeroOfForallPowDvd.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/EqZeroOfForallPowDvd.lean#L283), the diagonal matrix is `blk` at line 325 there, and primitive systems are `IsPrimitiveSystem` in EpsilonPairingZeta.lean. The two results of step 1 are `GlobalTheory.T.quasiLog_first_block_small_of_frobenius` and `GlobalTheory.T.small_mod_maximal_of_frobenius_image_small`; we read their statements only. The sentence about their content is a reading of their hypotheses, not of their proofs. In the proof in this file, the field $C$ is used only to take $p$-th roots; the chart, the basis and $\varepsilon$ enter only through these two results.
