---
title: The quotient index bound
decls:
  - GlobalTheory.ArcCM.qat_of_kill_detect
  - GlobalTheory.T.quotientBound_of_kill_detect_constantRoom
  - GlobalTheory.RunJoin.qAt_run
  - GlobalTheory.T.recursive_page_lattice_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The quotient index bound

Let $Q_m = M / (M \cap S^\flat)$. If forms $\theta_1, \ldots, \theta_\rho \in M$ span $S$ together with $S^\flat$ and have small sup norms, then the index of the span of their images in $Q_m$ is bounded by a polynomial in the size of the weight. This is the *quotient index bound*. First, numerically good functionals that detect $S^\flat$ give a *bridge* (Proposition (From good functionals to a bridge)), and a bridge gives the bound by a theorem of Volume 13. Second, the CM family of Sections 3 to 5 gives the bound under a room condition (Theorem (Quotient index bound from kill and detect)). Third, a page supplies the room (Theorem (Quotient index bound on a page)).

**Notation.** We keep the setting of Section 1, with a step $j$, a weight $\kappa$ and reals $C_R, T, c$. The module $M$ is a *lattice* if it is a finitely generated $\mathcal{O}_K$-submodule of $S$ that spans $S$ over $K$. Then $\rho_P$ is the rank of the torsion-free module $Q_m$. For a prime $\lambda$ of $\mathcal{O}_K$ we write $N\lambda$ for its norm and $\ell_\lambda$ for the length of a module after localization at $\lambda$. For $F \in S$ the *mean log sup* is $m(F) = \frac{1}{[K:\mathbb{Q}]} \sum_\sigma \log \|F\|_\sigma$, where $\sigma$ runs over the embeddings $K \to \mathbb{C}$. The size data of the core give a real number $z$ (the product of $f$, $r$ and a scale parameter $L$), two more numbers $k$ and $b$, and an integer $n_V$. For reals $C$ and $A$ we put $P(C, A) = C z^A$. The root discriminant of $K$ is $\mathrm{rd}_K = |d_K|^{1/[K:\mathbb{Q}]}$. The weight $\kappa$ is *last positive* if the last entry $a^+_{\tau,i}$ of each family $(a^+_{\tau,i})_i$ is at least $1$.

**Definition 4.6.1 (Quotient index bound).** Let $C_R, C_k, C_h, A_h, C_c, A_c, T, c$ be real numbers. The *quotient index bound* $Q(C_R, C_k, C_h, A_h, C_c, A_c, T, c)$ at $(j, \kappa)$ is the following statement. Assume that $C_R \geq 0$, that $\log [K:\mathbb{Q}] \leq P(C_h, A_h)$ and $\log \mathrm{rd}_K \leq P(C_h, A_h)$, that $n = n_V$, that $\kappa$ is last positive, that $\mathrm{size}(\kappa) \leq C_k\, k f b$, and that $T > 0$, $c > 0$ and $Tc \leq 1$. Then there is a function $\beta \geq 0$ on the primes of $K$ with finite support and

$$\frac{1}{[K:\mathbb{Q}]} \sum_\lambda \beta(\lambda) \log N\lambda \leq P(C_c, A_c)\, \mathrm{size}(\kappa),$$

with this property: for all $\theta_1, \ldots, \theta_{\rho_P} \in M$ such that the $K$-span of the $\theta_i$ and $S^\flat$ together span $S$, and such that $m(\theta_i) \leq P(C_h, A_h)\, \mathrm{size}(\kappa)$ for each $i$, there is a function $\nu$ on the primes of $K$ with finite support such that, for each $\lambda$, the length $\ell_\lambda\big(Q_m / \sum_i \mathcal{O}_K \bar{\theta}_i\big)$ is a natural number and

$$\ell_\lambda\Big(Q_m \big/ \textstyle\sum_i \mathcal{O}_K \bar{\theta}_i\Big) \leq \nu(\lambda) + \rho_P\, \beta(\lambda), \qquad \frac{1}{[K:\mathbb{Q}]} \sum_\lambda \nu(\lambda) \log N\lambda \leq \rho_P\, P(C_c, A_c)\, \mathrm{size}(\kappa).$$

Here $\bar{\theta}_i$ is the image of $\theta_i$ in $Q_m$. The sum $\sum_\lambda \ell_\lambda \log N\lambda$ is the logarithm of the index of $\sum_i \mathcal{O}_K \bar{\theta}_i$ in $Q_m$ (compare [Hermitian lattices](/learn/arakelov/#hermitian-lattices-and-slopes)).

**From good functionals to a bridge.** A *bridge* with constants $(C_h, A_h, C_c, A_c)$ is the datum of [Theorem 7.9.5 of Volume 13](/entry/qat-of-bridge-prime/) of Volume 13: a number field $K_1 \supset K$, $K_1$-linear forms $c_1, \ldots, c_{\rho_P}$ on $K_1 \otimes_K S$, a function $\beta \geq 0$ with finite support on the primes of $K$, functions $s_i$ on the primes of $K_1$ with finite support, functions $a_i$ on the infinite places of $K_1$, and reals $C_{\mathrm{arch}}$ and $B_{\deg}$. The conditions are: the common kernel of the $c_i$ is the $K_1$-span of $S^\flat$; $\beta$ satisfies the sum bound of the definition above; $-e(w|\lambda)\beta(\lambda) \leq \mathrm{ord}_w\, c_i(F) + s_i(w)$ for $F \in M$ with $c_i(F) \neq 0$; the sup norms satisfy $\|F\|_{\bar{\sigma}} = \|F\|_\sigma$; $\log |c_i(F)|_\sigma + a_i(\sigma) \leq \log \|F\|_{\sigma|_K} + C_{\mathrm{arch}}$; the normalized degree $\frac{1}{[K_1:\mathbb{Q}]}\big(\sum_w s_i(w) \log Nw - \sum_\sigma m_\sigma a_i(\sigma)\big)$ is at most $B_{\deg}$; and

$$P(C_h, A_h)\, \mathrm{size}(\kappa) + C_{\mathrm{arch}} + B_{\deg} + \tfrac{1}{2} \log \rho_P \leq P(C_c, A_c)\, \mathrm{size}(\kappa),$$

with $\log 0 = 0$. [Theorem 7.9.5 of Volume 13](/entry/qat-of-bridge-prime/) says: if $M$ is a lattice and a bridge exists, then the quotient index bound holds, for every value of $C_k$.

**Proposition 4.6.2 (From good functionals to a bridge).** Let $C_R, C_h, A_h, C_c, A_c, T, c, C_{\mathrm{arch}}, B_{\deg}$ be real numbers and $\beta$ a real function on the primes of $K$. Assume:

1. $M$ is a lattice;
2. $\beta \geq 0$, $\beta$ has finite support, and $\frac{1}{[K:\mathbb{Q}]} \sum_\lambda \beta(\lambda) \log N\lambda \leq P(C_c, A_c)\, \mathrm{size}(\kappa)$;
3. $\|F\|_{\bar{\sigma}} = \|F\|_\sigma$ for all $\sigma$ and all $F \in S$;
4. $P(C_h, A_h)\, \mathrm{size}(\kappa) + C_{\mathrm{arch}} + B_{\deg} + \frac{1}{2} \log \rho_P \leq P(C_c, A_c)\, \mathrm{size}(\kappa)$;
5. for each $F \in S$ with $F \notin S^\flat$ there are a number field $K_1 \supset K$ and a $K$-linear map $\varphi : S \to K_1$ with $S^\flat \subset \ker \varphi$ and $\varphi(F) \neq 0$, such that $\varphi$ is numerically good for $(M, \|\cdot\|, \beta, C_{\mathrm{arch}}, B_{\deg})$.

Then a bridge with constants $(C_h, A_h, C_c, A_c)$ exists.

Lean: `GlobalTheory.ArcCM.qbridge_of_numGood`.

*Proof.* Let $\mathcal{G}$ be the set of pairs $(K_1, \varphi)$ where $\varphi : S \to K_1$ is $K$-linear, kills $S^\flat$ and is numerically good. If $(K_1, \varphi) \in \mathcal{G}$ and $e : K_1 \to K_2$ is an embedding of number fields, then $(K_2, e \circ \varphi) \in \mathcal{G}$, by a lemma on the extension of numerically good functionals. If a vector $v \in S$ is killed by every member of $\mathcal{G}$, then $v \in S^\flat$, by hypothesis 5. A lemma of linear algebra on such sets of functionals gives a number field $K_1$ and members $\varphi_1, \ldots, \varphi_\rho$ of $\mathcal{G}$ over $K_1$ such that the common kernel of their $K_1$-linear extensions $c_i$ to $K_1 \otimes_K S$ is the $K_1$-span of $S^\flat$, and $\rho + \dim_K S^\flat = \dim_K S$. Since $M$ is a lattice, $\rho_P + \dim_K S^\flat = \dim_K S$, so $\rho = \rho_P$.

For each $i$, numerically good gives a good metrized line $N_i$ over $K_1$. Put $s_i(w) = -v_w(I_{N_i})$ and $a_i(\sigma) = \log n_{N_i, \sigma}$. Each $s_i$ has finite support, since $I_{N_i}$ has finitely many prime factors. The finite condition of the bridge is condition 3 of numerically good, and the archimedean condition is condition 4. For the degree, a lemma on good lines with $n_{N, \bar{\sigma}} = n_{N, \sigma}$ gives

$$\frac{1}{[K_1:\mathbb{Q}]}\Big(\sum_w s_i(w) \log Nw - \sum_\sigma m_\sigma\, a_i(\sigma)\Big) = \widehat{\deg}\, N_i,$$

and condition 1 of numerically good gives $\widehat{\deg}\, N_i \leq B_{\deg}$. The remaining conditions are hypotheses 2, 3 and 4. $\square$

**Room.** In the setting of Sections 3 to 5, with $n_{\mathrm{At}}$ from Section 3 and $C_{\mathrm{At}}$, $B_{\mathrm{At}}$ from Section 5, we say that the constants $(C, A)$ have *room* if

$$C_{\mathrm{At}} \leq P(C, A)\, \mathrm{size}(\kappa), \qquad B_{\mathrm{At}} \leq P(C, A)\, \mathrm{size}(\kappa), \qquad \log |d_E| + \log n_{\mathrm{At}} \leq P(C, A).$$

**Theorem 4.6.3 (Quotient index bound from kill and detect).** Assume $\mathcal{K}$ and the laws of the core, and the principal level hypothesis of Section 3. Let $j < m$ be in the admissible range, $\kappa$ a weight, and $C_R, T, c, C_k, C_h, A_h, C_0, A_0, C_d, A_d$ real numbers. Assume:

1. $M$ is a lattice;
2. the CM family at $(j, \kappa, C_R, T, c)$ kills and detects $S^\flat(C_R, T, c)$;
3. $z \geq 1$, $C_0 \geq 0$ and $C_d \geq 0$;
4. the constants $(C_0, A_0)$ have room;
5. $\log \dim_K S \leq P(C_d, A_d)\, \mathrm{size}(\kappa)$.

Then the quotient index bound $Q(C_R, C_k, C_h, A_h, C_h + 3C_0 + C_d, \max(A_h, A_0, A_d), T, c)$ holds at $(j, \kappa)$.

Lean: `GlobalTheory.ArcCM.qat_of_kill_detect` (also `GlobalTheory.T.quotientBound_of_kill_detect_constantRoom`, a second name).

*Proof.* Put $C_c = C_h + 3C_0 + C_d$ and $A_c = \max(A_h, A_0, A_d)$, and assume the hypotheses of the quotient index bound. We make a bridge with the proposition.

Step 1. $C_h \geq 0$. Since $[K:\mathbb{Q}] \geq 1$, we have $0 \leq \log [K:\mathbb{Q}] \leq C_h z^{A_h}$, and $z^{A_h} > 0$.

Step 2. The error function. Let $\beta = \beta_{E, n_{\mathrm{At}}, \mathrm{abs}(a'_\kappa)}$ be the local error of Section 4. Then $\beta \geq 0$. By the pins of the core, $\mathrm{abs}(a'_\kappa) + f n \leq \mathrm{size}(\kappa)$, so $\mathrm{abs}(a'_\kappa) \leq \mathrm{size}(\kappa)$. We have $n_{\mathrm{At}} \geq 1$. Since $m_\lambda(E, n') \leq v_\lambda(|d_E|) + v_\lambda(n')$ and $\sum_\lambda v_\lambda(x) \log N\lambda = [K:\mathbb{Q}] \log x$ for a positive integer $x$, a lemma on $\beta$ gives that $\beta$ has finite support and

$$\frac{1}{[K:\mathbb{Q}]} \sum_\lambda \beta(\lambda) \log N\lambda \leq \big(\log |d_E| + \log n_{\mathrm{At}}\big)\, \mathrm{abs}(a'_\kappa) \leq P(C_0, A_0)\, \mathrm{size}(\kappa),$$

by the third room inequality.

Step 3. $\log \rho_P \leq \log \dim_K S$, since $\rho_P + \dim_K S^\flat = \dim_K S$ and $\log 0 = 0$.

Step 4. The room of the bridge. Let $u = \mathrm{size}(\kappa) \geq 0$. Since $z \geq 1$, we have $z^A \leq z^{A_c}$ for $A \in \{A_h, A_0, A_d\}$. With $C_h, C_0, C_d \geq 0$, the first two room inequalities, Step 3 with hypothesis 5, and Step 2, this gives

$$\begin{aligned} C_h z^{A_h} u + C_{\mathrm{At}} + B_{\mathrm{At}} + \tfrac{1}{2} \log \rho_P &\leq (C_h + 3C_0 + C_d)\, z^{A_c} u, \\ \frac{1}{[K:\mathbb{Q}]} \sum_\lambda \beta(\lambda) \log N\lambda &\leq (C_h + 3C_0 + C_d)\, z^{A_c} u. \end{aligned}$$

Here $\frac{1}{2} \log \rho_P \leq C_d z^{A_c} u$, since $\log \rho_P \leq C_d z^{A_c} u$ and the right side is not negative.

Step 5. A lemma on the recursive construction gives $\|F\|_{\bar{\sigma}} = \|F\|_\sigma$.

Step 6. Hypothesis 5 of the proposition, with $C_{\mathrm{arch}} = C_{\mathrm{At}}$ and $B_{\deg} = B_{\mathrm{At}}$. Let $F \in S$ with $F \notin S^\flat$. Since the family detects $S^\flat$, there are a number field $K_1 \supset K$ and $d \in \mathrm{Fam}_Q$ over $K_1$ with $\mathrm{cf}_d(F) \neq 0$. [Theorem (The CM functionals are numerically good)](/entry/num-good-of-fam-q/) gives a $K$-linear $\varphi : S \to K_1$ with $\varphi = \mathrm{cf}_d$ on $S$ that is numerically good for $(M, \|\cdot\|, \beta, C_{\mathrm{At}}, B_{\mathrm{At}})$. Since the family kills $S^\flat$, we have $S^\flat \subset \ker \varphi$. And $\varphi(F) = \mathrm{cf}_d(F) \neq 0$.

The proposition now gives a bridge with constants $(C_h, A_h, C_c, A_c)$, and [Theorem 7.9.5 of Volume 13](/entry/qat-of-bridge-prime/) gives the quotient index bound. $\square$

**The bound on a page.** On a page of the recursive construction, all conditions of the last theorem except the lattice condition follow from the page data. A *page* at $(j, \kappa)$ is a list of conditions on the size data, on a record $H$ of constants $C_K, C_A, \ldots$, on reals $C_2, A_2, C_T, h_0$, on weights $\kappa, w_L, w_F$ and on natural numbers $T_n, n_P, n_W$. They include the family hypotheses (with a parameter bound for the constant $C_A$), a page bound (with $\log N\mathfrak{c} \leq L$ for the conductor ideal $\mathfrak{c}$), ties between the constants of $H$ and $(C_2, A_2, 7)$, and $r \geq 8$. The page also fixes a real number $c_{\mathrm{pg}}$, computed from $C_2, A_2, w_L$ and $C_R = 7$.

**Theorem 4.6.4 (Quotient index bound on a page).** There is a function $C_q : \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ with the following property. Let the datum, a top of the recursive construction with its laws, an admissible step $j$, size data and the data of a page at $(j, \kappa)$ be given. Assume that the page conditions hold, that $j < m$, and that $M$ is a lattice. Then the quotient index bound

$$Q\big(7,\ C_K,\ 1,\ 4,\ C_q(C_A, C_K),\ 4,\ T_n,\ c_{\mathrm{pg}}\big)$$

holds at $(j, \kappa)$.

Lean: `GlobalTheory.RunJoin.qAt_run` (also `GlobalTheory.T.recursive_page_lattice_bound`, a second name).

*Proof.* A lemma on the run constants gives a function $C_0(a, b, c) \geq 0$ with this property: if the parameter bound holds with $C_A$, $\log N\mathfrak{c} \leq L$, $j$ is admissible, $j < m$, $r \geq 3$, $C_R \geq 0$, $\mathrm{size}(\kappa) \leq C_k\, k f b$, $T > 0$, $c > 0$ and $Tc \leq 1$, then $z \geq 1$ and the constants $(C_0(C_A, C_R, C_k), 4)$ have room. We put

$$C_q(a, b) = 1 + 3\, C_0(a, 7, b) + 1041.$$

Assume the hypotheses of the quotient index bound with $C_R = 7$, $C_k = C_K$, $T = T_n$ and $c = c_{\mathrm{pg}}$. Since $r \geq 8$ and the page gives the parameter bound and $\log N\mathfrak{c} \leq L$, the lemma gives $z \geq 1$ and room for $(C_0(C_A, 7, C_K), 4)$.

A theorem on the theta net of the page, proved outside this chapter, gives $\log \dim_K S \leq 1041\, z^3$. Since $\mathrm{size}(\kappa) \geq 1$, this is at most $P(1041, 3)\, \mathrm{size}(\kappa)$.

The laws of the top give the laws of the core and the principal level hypothesis, and $\mathcal{K}$ holds by a theorem proved outside this chapter. The CM family kills $S^\flat$: for $F \in S^\flat$, Theorem (Low coefficients) gives $F_k \in \mathrm{SS}_{>c_1}(\lambda_k)$ for all $k$, and a lemma on CM arc functionals then gives $\mathrm{cf}_d(F) = 0$ for $d \in \mathrm{Fam}_Q$. The CM family detects $S^\flat$ by [Theorem (The CM family detects low coefficients)](/entry/cm-family-functionals-detect-low-coefficients/), since $r \geq 3$, $T > 0$ and $c > 0$.

So Theorem (Quotient index bound from kill and detect) applies with $C_h = 1$, $A_h = 4$, $C_0 = C_0(C_A, 7, C_K)$, $A_0 = 4$, $C_d = 1041$ and $A_d = 3$. It gives the quotient index bound with $C_c = 1 + 3C_0(C_A, 7, C_K) + 1041 = C_q(C_A, C_K)$ and $A_c = \max(4, 4, 3) = 4$. We apply it to the hypotheses that we assumed. $\square$

**Remark 4.6.5 (Formalization).** The quotient index bound is `QAt` ([WeightedPrimeSumBound.lean](lean:Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/WeightedPrimeSumBound.lean#L38)) and room is `RoomAt`. In `qat_of_kill_detect` ([QuotientBoundOfKillDetectConstantRoom.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/QuotientBoundOfKillDetectConstantRoom.lean#L51)) the constant $C_k$ is only passed to the conclusion, and of the hypotheses of the quotient index bound the proof uses only $\log [K:\mathbb{Q}] \leq P(C_h, A_h)$; the others go unused to the bridge theorem. In `qAt_run` ([RecursivePageLatticeBound.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/RecursivePageLatticeBound.lean#L35)) the parameter $T$ is the natural number $T_n$, so the theorem covers only integer values of $T$. The second name `recursive_page_lattice_bound` ([RecursivePageLatticeBoundStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/RecursivePageLatticeBoundStatement.lean#L22)) speaks of a lattice bound, but the lattice property is a hypothesis and the conclusion is `QAt`. The proof that the family kills $S^\flat$ is `killQ_of_gamAt`, in a file named for another lemma ([ExistsExtendEmbedding.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/ExistsExtendEmbedding.lean#L21)). The second names are wrappers. We have not unfolded $C_0$, the page conditions, the theta net theorem or the linear algebra lemma.

## Notes and references

The quotient index bound on a page is an input of [the theorem that assembles the index bound hypotheses](/entry/inputs-net-rec-plus/), which gives the constant $C_q$ and the condition $Q$ at each run. That theorem is the main part of [the run theorem](/entry/run-holds-of-par-ok/), and both are in branch 2 of [the unitary hypotheses step](/proof/unitary-hypotheses/).

For Fourier-Jacobi expansions and toroidal compactifications, see Faltings and Chai, *Degeneration of Abelian Varieties*, Springer 1990, Chapter V, and Lan, *Arithmetic Compactifications of PEL-Type Shimura Varieties*, Princeton 2013. For CM points and the algebraicity of their values, see Shimura, *Abelian Varieties with Complex Multiplication and Modular Functions*, Princeton 1998. For the Cauchy inequalities on polydiscs, see Hörmander, *An Introduction to Complex Analysis in Several Variables*, Chapter II.
