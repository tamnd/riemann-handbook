---
title: CM functionals detect low coefficients
decls:
  - GlobalTheory.ArcDetect.exists_fam_cfOf_ne_zero
  - GlobalTheory.T.exists_familyMember_functional_ne_zero
  - GlobalTheory.ArcCM.detectQ_of_known
  - GlobalTheory.T.cmFamilyFunctionals_detect_lowCoefficients
status: drafted
drafted_by: writer@claude-opus-5-5
---
## CM functionals detect low coefficients

This section defines the functionals of the chapter. Each one takes a cusp form $F$, evaluates it along a formal arc through a CM point, and reads off one coefficient of the result. The arcs come in a family, cut out by explicit bounds on the level $n'$ of the CM point and on the length $\Lambda_0$ of its letters. The main result is that this family *detects* the subspace $S^\flat$: if every functional of the family vanishes on $F$, then $F \in S^\flat$ (Theorem (The CM family detects low coefficients)). The proof combines Theorem (Low coefficients) of Section 1 with the split point of Section 2. The result is one of the two inputs of [Theorem 4.6.3](/entry/qat-of-kill-detect/), and it is also used directly in [the theorem that assembles the index bound hypotheses](/entry/inputs-net-rec-plus/).

**Arcs and coefficient functionals.** Let $K_1$ be a number field that contains the field of coefficients $K$. An *arc datum* $d$ over $K_1$ consists of a model of the moduli space over a valuation ring, a point of it with an arc through the point (a formal curve over $K_1[[t]]$, given by tangent vectors $e_{\tau,k}$ for the embeddings $\tau$ of $E$ and $k$ below the multiplicity of $\tau$), a nonzero theta section $\theta$, a framed point $y_F$ on the arc, an integer $j_d$, and a monomial $X^\mu$ in the letters $X_{\tau,i,l}$ (one letter for each $\tau$ and each pair $i, l$ below the multiplicity of $\tau$). Let $F$ be a section of weight $(a', n)$. Its evaluation at $y_F$ lies in a ring of functions on the arc, which receives the polynomial ring $K_1((t))[X_{\tau,i,l}]$ in the letters over the Laurent series. Let $N_F$ be a chosen polynomial in this ring that maps to the evaluation, and $N_F = 0$ if there is none.

**Definition 4.3.1 (Coefficient functional).** The coefficient functional of the arc datum $d$ is

$$\mathrm{cf}_d(F) = \big[\, X^\mu t^{j_d} \,\big]\, N_F \in K_1,$$

the coefficient of $t^{j_d}$ in the coefficient of $X^\mu$ of $N_F$.

Section 5 shows that $\mathrm{cf}_d$ is $K$-linear in $F$. The arc data that we use satisfy two kinds of conditions. The first kind is local. An arc datum is *standard* if it lies over the base, its framing is normalized at level $1$, and the pushforward of its line bundle is invertible. The second kind is the CM condition.

**Definition 4.3.2 (CM input).** Let $d$ be an arc datum over $K_1$, let $n' \in \mathbb{N}$ and $\Lambda_0, c_1 \in \mathbb{R}$. A *CM input* for $d$ with parameters $(n', \Lambda_0, c_1)$ consists of:

1. polarized [abelian schemes](/learn/theta-functions-cm/#abelian-varieties-with-complex-multiplication) over $\mathcal{O}_{K_1}$ with an action of $\mathcal{O}_E$, and homomorphisms between them and the abelian scheme of the point of $d$, which commute with the action of $\mathcal{O}_E$;
2. metrized lines $T$ and $\ell_m$ over $K_1$ (defined in Section 4), such that the whole object is good at the bound $\Lambda_0$, and a good set of letters $m$ with lines $\ell_m$;
3. a level $n' > 0$ with a canonical twist at level $n'$, and a splitting at level $n'$;
4. a nonzero $\mathbb{Z}$-linear form $\xi$ on an $\mathcal{O}_E$-module of rank one of the point, and an element $\nu_0 \in E$ with $\mathrm{Tr}_{E/\mathbb{Q}}(\nu_0)/2 \leq c_1$ that is tied to $\xi$ and to $j_d$ by a condition at the level of the moduli space;
5. for each tangent vector $e_{\tau,k}$ a kind: either the vector is a logarithmic tangent given by the form $\xi$, or it is the pullback of a letter $m$ of the CM abelian scheme along multiplication by $1/n'$. For each $\tau$ at least one vector has the first kind, and the letters used for $\tau$ are exactly the letters of $\tau$, each once.

For each $(\tau, k)$ the CM input gives a metrized line $\ell(\tau, k)$: the trivial line for a vector of the first kind and the line $\ell_m$ of its letter for the second kind.

**Definition 4.3.3 (The CM family).** Let $n' \in \mathbb{N}$ and $\Lambda_0, c_1 \in \mathbb{R}$. An arc datum $d$ is in the *family* $\mathrm{Fam}(n', \Lambda_0, c_1)$ if it is standard and has a CM input with parameters $(n', \Lambda_0, c_1)$. In the setting of Section 1, with $j < m$, a weight $\kappa$ and $C_R, T, c$, we put

$$n_{\mathrm{At}} = n_Q\big(E, r, g_0 g_1, |d_E|, N(\mathfrak{c}), c_1, \mathrm{size}(\kappa) + r\big), \qquad \Lambda_{\mathrm{At}} = \Lambda_Q\big(E, r, \rho_j, g_0 g_1, |d_E|, N(\mathfrak{c}), c_1, \mathrm{size}(\kappa) + r\big),$$

with $n_Q$ and $\Lambda_Q$ as in Section 2, $c_1 = c_1(C_R, T, c, j)$, $g_0 g_1$ the level of the datum and $\mathfrak{c}$ its conductor ideal. The family $\mathrm{Fam}_Q = \mathrm{Fam}(n_{\mathrm{At}}, \Lambda_{\mathrm{At}}, c_1)$ is the *CM family* at $(j, \kappa, C_R, T, c)$.

**Definition 4.3.4 (Kill and detect).** The CM family *kills* $S^\flat$ if $\mathrm{cf}_d(F) = 0$ for every number field $K_1 \supset K$, every $d \in \mathrm{Fam}_Q$ over $K_1$ and every $F \in S^\flat$. It *detects* $S^\flat$ if every $F \in S$ with $\mathrm{cf}_d(F) = 0$ for all such $K_1$ and $d$ lies in $S^\flat$.

If both hold, then $S^\flat$ is exactly the common kernel of the functionals of the family. We use two families of statements that are proved outside this chapter. The first is a list $\mathcal{K}$ of fourteen statements: laws of degenerations and of uniform base change, a uniformization of theta functions, the toroidal archimedean condition, the extension of homomorphisms over discrete valuation rings, a key formula, the existence of CM points, a degree statement and laws of evaluation. The second is the existence of models: for each prime $p$ and each valuation subring $W \subset \mathbb{C}$ in which $p$ is not a unit, there is a model of the moduli space over $W$ with the property $N_4$ and an invertible pushforward. Under $\mathcal{K}$ the second follows from a good level, and we use it in this form.

**Theorem 4.3.5 (A family member that sees a form).** Assume $\mathcal{K}$. Let $U$ be a unitary chart of the moduli space at the base embedding, $k$ a component, and $X$ a Hermitian datum with extra data as in Section 2 whose underlying datum is $X_k$. Let $\mathfrak{A}$ be a fractional ideal of $E$, $(a', n)$ a weight and $c_1, w \in \mathbb{R}$. Assume:

1. the moduli space has models at all primes, $U$ is a uniformization, the level of the moduli space has $A = 1$, and $r \geq 3$;
2. for each component the group $\Gamma$ contains every unitary element that stabilizes $\Lambda$ and is congruent to $1$ modulo $M$ on $\Lambda$ (we say that $U$ has principal level $M$), $a'$ is decreasing in its second argument and $n$ is even, and $\chi_{\lambda_{k'}} = 1$ on $\Gamma$ for every component $k'$;
3. $\mathfrak{A} \neq 0$, the lattice $\Lambda$ of $X$ is the $\mathcal{O}_E$-span of the products $a u$ with $a \in \mathfrak{A}$ and $u \in L'$, and $g = M$, the level of the moduli space;
4. $c_1 > 0$ and $\mathrm{abs}(a') + f n + r \leq w$, where $\mathrm{abs}(a') = \sum_\tau \sum_i a'(\tau, i)$, summed over $i$ below the multiplicity of $\tau$.

Let $F$ be a section of weight $(a', n)$ with $F_{k'} \in \mathrm{SS}(\lambda_{k'})$ for every component $k'$ and $F_k \notin \mathrm{SS}_{>c_1}(\lambda_k)$. Then there are a number field $K_1 \supset K$ and an arc datum $d$ over $K_1$ with

$$d \in \mathrm{Fam}\big(n_Q(E, r, M, N_A, N_C, c_1, w),\ \Lambda_Q(E, r, q, M, N_A, N_C, c_1, w),\ c_1\big) \quad \text{and} \quad \mathrm{cf}_d(F) \neq 0.$$

Lean: `GlobalTheory.ArcDetect.exists_fam_cfOf_ne_zero` (also `GlobalTheory.T.exists_familyMember_functional_ne_zero`, a second name).

*Proof.* Step 1: a split point. The weight $\lambda_k$ is dominant since $a'$ is decreasing, a lemma on the weights of a uniformization bounds its total spread so that the bound $\mathrm{abs}(a') + fn + r \leq w$ gives $\sum_\tau \mathrm{spread}_\tau(\lambda_k) \leq w$, and $1 \leq 3 \leq r \leq w$. So Corollary (Split points with the constants of the CM family) applies to $F_k$. It gives an isotropic $\xi$, a $\nu$ with $\sum_\tau \nu_\tau \leq c_1$, a point $x$ of the domain and vectors $\ell_i$ with split data for $\Lambda_Q$, the torsion condition at level $n_Q$, and $\mathrm{FJ}_{\xi,\nu}(F_k)(x) \neq 0$.

Step 2: the frequency is a CM value. Since the coefficient is not zero and $F_k$ is a cusp form, there is $\nu_0 \in E$ with $\nu_\tau = \mathrm{Re}\, \tau(\nu_0)$ for all $\tau$, which is integral in the sense of the period lattice of $\xi$. The sum of $\mathrm{Re}\, \tau(\nu_0)$ over a CM type is $\mathrm{Tr}_{E/\mathbb{Q}}(\nu_0)/2$, so $\mathrm{Tr}_{E/\mathbb{Q}}(\nu_0)/2 \leq c_1$.

Step 3: the CM point. The chart is a uniformization, so it has a witness, and the principal level gives the transversality of the weight on each component: the transvections along isotropic vectors that are congruent to $1$ lie in $\Gamma$ and $\chi$ is trivial on them. The existence of CM data at a split isotropic point, a theorem proved outside this chapter from $\mathcal{K}$, now gives a number field $K_1$, an embedding $\varepsilon : K_1 \to \mathbb{C}$ over the base embedding, an arc with tangent vectors $e$, a theta section $\theta$, an integer $j_d$ and a CM input $s$ with parameters $(n_Q, \Lambda_Q, c_1)$ and element $\nu_0$. It also gives a comparison: at $\varepsilon$, the arc matches the frame $x$ of the chart along $\xi$.

Step 4: a model and an arc datum. We choose the prime $2$ and a valuation subring of $\mathbb{C}$ in which $2$ is not a unit. The existence of models gives a model $Y$ over it with $N_4$ and an invertible pushforward. The construction of arc data (from the laws in $\mathcal{K}$ and the fact that the CM letters form a Lie basis along the arc) gives an arc datum $d_0$ over $K_1$ with the arc, $\theta$ and $j_d$ of Step 3, the monomial $X^0$, and a model that lies over the base and is normalized. So $d_0$ is standard, and $s$ is a CM input for it.

Step 5: a monomial. The Fourier-Jacobi coefficient $\mathrm{FJ}_{\xi,\mathrm{Re}\,\tau(\nu_0)}(F_k)(x)$ is not zero by Step 1. The comparison of Step 3 identifies it with a value of the evaluation of $F$ along the arc of $d_0$. Then a theorem proved outside this chapter (a nonzero Fourier-Jacobi coefficient at a CM arc gives a nonzero coefficient of the arc) gives a monomial $X^{\mu}$ with $[X^{\mu} t^{j_d}] N_F \neq 0$. Let $d$ be $d_0$ with $X^0$ replaced by $X^\mu$. Standardness and the CM input do not depend on the monomial, so $d \in \mathrm{Fam}(n_Q, \Lambda_Q, c_1)$ and $\mathrm{cf}_d(F) \neq 0$. $\square$

**Theorem 4.3.6 (The CM family detects low coefficients).** Assume $\mathcal{K}$ and the laws of the core. Assume that the chart at each good embedding and each admissible step has principal level $M$. Let $j < m$ be in the admissible range, let $\kappa$ be a weight, and let $C_R, T, c$ be real numbers with $T > 0$ and $c > 0$. Assume $r \geq 3$. Then the CM family at $(j, \kappa, C_R, T, c)$ detects $S^\flat(C_R, T, c)$.

Lean: `GlobalTheory.ArcCM.detectQ_of_known` (also `GlobalTheory.T.cmFamilyFunctionals_detect_lowCoefficients`, a second name).

*Proof.* Let $F \in S$ with $\mathrm{cf}_d(F) = 0$ for all $d \in \mathrm{Fam}_Q$, and suppose $F \notin S^\flat$. By Theorem (Low coefficients), every $F_{k'}$ is a cusp form, and there is a component $k$ with $F_k \notin \mathrm{SS}_{>c_1}(\lambda_k)$.

We check the hypotheses of Theorem (A family member that sees a form) at $k$. The datum gives a fractional ideal $\mathfrak{A}$ of $E$, which is nonzero by a lemma on principal data, and a lemma gives an extended Hermitian datum $X$ on $X_k$ with $\Lambda = \mathfrak{A} L'$, $g = g_0 g_1$, $N_A = |d_E|$ and $N_C = N(\mathfrak{c})$. The numerics of the pins of the core give a good level, $A = 1$, $q = \rho_j$, $M = g_0 g_1$ and the bound $\mathrm{abs}(a') + fn \leq \mathrm{size}(\kappa)$; the good level gives models at all primes. The laws give the uniformization and $\chi_{\lambda_{k'}} = 1$, and the hypothesis gives the principal level. For $c_1$ we have $c_1 > 0$, since $\mathrm{rd}_E^{C_R} > 0$, $T, c > 0$, $f > 0$ and $\rho_j = m - j > 0$. We take $w = \mathrm{size}(\kappa) + r$.

The theorem gives $K_1$ and $d$ with $\mathrm{cf}_d(F) \neq 0$ in the family with parameters computed from $(E, r, M, N_A, N_C, c_1, w)$ and $q$. With $M = g_0 g_1$, $N_A = |d_E|$, $N_C = N(\mathfrak{c})$ and $q = \rho_j$ these are $n_{\mathrm{At}}$ and $\Lambda_{\mathrm{At}}$, so $d \in \mathrm{Fam}_Q$. This contradicts $\mathrm{cf}_d(F) = 0$. $\square$

**Remark 4.3.7 (Formalization).** The functional is $\mathrm{cfOf}$ of [FunDef.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ArchimedeanQuadraticData/ArcLineFunctions/FunDef.lean#L9), and the polynomial $N_F$ is a choice (`arcNum`): if the evaluation has no preimage, it is $0$. The family $\mathrm{Fam}_Q$ puts no condition on the monomial $\mu$ or on $j_d$. The proof of the first theorem builds the arc datum with the monomial $0$ and then replaces it ([ExistsFamilyMemberFunctionalNeZero.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/ExistsFamilyMemberFunctionalNeZero.lean#L199), line 208), and the prime $2$ in Step 4 is an arbitrary choice (line 195). The list $\mathcal{K}$ is the structure `Known`, and we have not unfolded its fields, the arc datum, the model conditions, or the fields of `CMIn` beyond their statements. The principal level is the hypothesis `GamAt` of the core.
