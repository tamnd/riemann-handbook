---
title: A slope bound for the glued lattice of an indefinite form
decls:
  - Formalism.L2.Indef.Tree.functional_lower_bound_of_conditions_numeric
  - Formalism.L2.Indef.Tree.functional_lower_bound_of_conditions
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A slope bound for the glued lattice of an indefinite form

The lattices of the indefinite side of the theta argument are glued from local pieces, one type of piece for each finite place, and the argument needs an upper bound for their [maximal slope](/learn/arakelov/#hermitian-lattices-and-slopes). This section proves such a bound by the slope inequality of Bost: a matrix $\Psi$ maps the glued lattice injectively into a fixed lattice $M$ up to explicit denominators, so its maximal slope is bounded by that of $M$, the archimedean size of $\Psi$ and the size of the denominators. The inputs are numeric conditions, and the bound is $x^{C_H} b$. The result is used in [Theorem](/entry/fun0-fit-of-leaves-alt/).

### Notation

Let $K$ be a totally complex number field with $n_K$ infinite places, so $[K : \mathbb{Q}] = 2 n_K$. For a finite place $w$ write $v_w$ for its valuation and $\ell_w = \log \mathrm{N}w / [K : \mathbb{Q}]$. A frame on $K^D$ is a family $X = (X_v)$ of invertible complex $D \times D$ matrices, one for each infinite place $v$; it defines a hermitian norm $|\cdot|_{X,v}$ at $v$, making each $\mathcal{O}_K$-lattice in $K^D$ a hermitian lattice. We write $\hat\mu_{\max}(L, X)$ for $2\mu_{\max} - \log 2 + \log|\Delta_K|/[K:\mathbb{Q}]$, where $\mu_{\max}$ is the maximal slope of this hermitian lattice. For a $K$-linear map $\varphi$ between spaces with frames $X$ and $X'$, its archimedean height is
$$h_\infty(\varphi; X, X') = \frac{1}{n_K} \sum_v \log \|\varphi\|_v^2,$$
where $\|\varphi\|_v$ is the operator norm for $|\cdot|_{X,v}$ and $|\cdot|_{X',v}$. For a positive function $\kappa$ on the infinite places put $\mathrm{mlog}\,\kappa = n_K^{-1} \sum_v \log \kappa_v$, and write $X^\kappa$ for the frame $\kappa_v^{1/2} X_v$, whose squared norms are those of $X$ divided by $\kappa_v$. For a function $g$ on the infinite places put $\mathrm{mean}_\infty g = n_K^{-1} \sum_v g_v$.

### The data

The indefinite datum $S$ has a dimension $D > 0$, a frame $X_E$ on $K^D$, a positive function $\kappa$ on the infinite places, a map $\mu$ from the finite places to a finite set of types with a base type $\mu_0$, a finite set $T_S$ of finite places, and for each type $t$ a matrix $\iota_t$ of size $D \times d_Q(t)$. The side datum gives, for each type $t$, a lattice $M_t$ and a surjective matrix $P_t$ with $d_Q(t)$ rows; put $\Lambda_t = P_t M_t$ and $U_t = \ker P_t$. The glued lattice $R$ is the lattice whose localization at $w$ is that of $\iota_{\mu(w)} \Lambda_{\mu(w)}$.

The target datum $O$ has a dimension $n$, a frame $X'$ on $K^n$, a lattice $M \subseteq K^n$, matrices $v_t$ of size $n \times n_V(t)$, a finite set $T_f$ of finite places with integers $d_F(w)$, integers $m, N, f, k$ and further integer and real parameters, and elements $r_{ij}(t)$ of $K$ indexed by $t$ and $(i,j) \in \{1, \dots, m\}^2$. For $C, x, b > 0$ the datum defines explicit constants $E_M(C)$, $b_{FP}$, $b_{IP}^a$, $b_{IP} = b_{IP}^a + 3 C f m N^2 \log b$, $b_{\mathrm{arch}}$, $b_\delta$, $b_{TH} = C f b (\log b + \log x)$, and
$$\mathrm{pol}(C, b) = 10^5 C^3 f m^2 N^2 \bigl( r N \log b + P(C, b) \bigr),$$
with $r = k + m - 1$ and $P(C, b) = C f^2 (k+m)^6 \log\bigl(b\,(k+m)\, g_1 g_2\, p\, p'\, |d_E|\bigr)$ for further integer parameters $g_1, g_2, p, p', d_E$ of $O$.

### The slope inequality

**Theorem 2.10.1 (Slope inequality).** Let $\bar E$ and $\bar F$ be hermitian vector bundles over $\mathrm{Spec}\,\mathcal{O}_K$ and $\varphi : E_K \to F_K$ an injective $K$-linear map. Then
$$\hat\mu_{\max}(\bar E) \le \hat\mu_{\max}(\bar F) + \sum_{\text{all places } v} \frac{[K_v : \mathbb{Q}_v]}{[K:\mathbb{Q}]} \log \|\varphi\|_v.$$
This is in Bost, *Périodes et isogénies des variétés abéliennes sur les corps de nombres*, Séminaire Bourbaki Exp. 795, §4.

**Remark 2.10.2.** In Lean the finite part of the height is an inclusion $\Psi R \subseteq \bigl(\prod_{w \in T} w^{-a(w)}\bigr) M$, which bounds $\log\|\Psi\|_w$ by $a(w) \log \mathrm{N}w$ and contributes $2\sum_T \ell_w a(w)$ after the normalisation. The archimedean height is taken for the frame $X_E^\kappa$, at the cost $-\mathrm{mlog}\,\kappa$. The form proved reads: if $R$ is a lattice in $K^D$, $M$ is nonzero and finitely generated, $\Psi$ is injective, the inclusion holds, $a(w) \le v_w(r_w) + d_F(w)$ on $T$, and the four sums are bounded by $E_M$, $h$, $G$, $B_F$, then
$$\hat\mu_{\max}(R, X_E) \le -\mathrm{mlog}\,\kappa + E_M + h + 2(G + B_F).$$
Lean: `Formalism.AtG.grid_function_bound`.

### The theorem

**Theorem 2.10.3 (Slope bound for the glued lattice).** Let $C, x, C_H, b$ be real numbers with $C \ge 1$, $x \ge 1$, $\log b \ge 1$ and $\log x \le 2 \log b$. Assume that the side datum is well formed, $D > 0$, every $\mu(\bar w) = \mu(w)$ and $T_S = \{w : \mu(w) \ne \mu_0\}$, the frames $X_E$ are invertible, $\iota_{\mu_0}$ maps the parts of the base type onto the parts of $K^D$, every $\iota_t$ is bijective, $\kappa > 0$, and at the base type $\iota_{\mu_0}$ multiplies the hermitian form on the part $Q_p$ by $\kappa_v \prod_j \lambda_j(p, v)$ with all $\lambda_j > 0$. Assume that $R$ is a lattice with the local description above. Assume finally the following conditions on $O$.

1. $M$ is finitely generated and nonzero, $X'$ is invertible, and $\hat\mu_{\max}(M, X') \le E_M(C)$.
2. There is an $n \times D$ matrix $\Psi$ with $\Psi \iota_t P_t = \bigl(\prod_{ij} r_{ij}(t)\bigr)^{-1} v_t$ for $t = \mu_0$ and for every $t$ in the image of $\mu$.
3. $\ker v_{\mu_0} = U_{\mu_0}$.
4. At every $w$ the localization of $v_{\mu(w)} M_{\mu(w)}$ lies in that of $w^{-d_F(w)} M$, $d_F = 0$ off $T_f$, and $2\sum_{T_f} \ell_w d_F(w) \le b_{FP}$.
5. Every $V$ with $V P_{\mu_0} = v_{\mu_0}$ has $h_\infty(V; X_Q, X') \le b_{IP}^a$, and there is $g$ with $g_v \le \sum_j \log \lambda_j(p, v)$ for every nonzero part $p$ and $\mathrm{mean}_\infty g \ge -3 C f m N^2 \log b$.
6. $r_{ij}(\mu_0) = 1$, every $r_{ij}(\mu(w)) \ne 0$, a few bookkeeping conditions on the integer indices hold, and $v_w(r_{ij}(\mu(w)))$ is bounded by an explicit sum of valuations of auxiliary elements $z_A, z_A', z_T, z_T'$ of $K$ and of weights attached to finite sets of primes, as in the grid estimate of the volume on exponent grids.
7. There is $\delta \ge 0$ on the finite places with $\sum_F \ell_w \delta_w \le b_\delta$ for every finite $F$; $z_A$ and $z_A'$ are nonzero with $v_w \ge -3\delta_w$ and $\mathrm{mean}_\infty \log^+ |\cdot|_v \le b_{\mathrm{arch}}$; $z_T$ and $z_T'$ are nonzero and their twisted heights are at most $b_{TH}$; and the prime counting sums are at most $b_{TH}$.
8. The size conditions: $2 \le m$, $m + 3 \le k$, $m^4 \le f \le k$, a lattice constant $L_c \le b$, $m f N^2 \le b$ with four more bounds of the same kind, two bounds on prime powers and on the sum $c_S \le 45 f \log b$, $1 \le B_w \le C b$ with $\log B_w \le C \log b$, and $\mathrm{pol}(C, b) \le x^{C_H}$.

Then
$$\hat\mu_{\max}(R, X_E) \le x^{C_H}\, b - \mathrm{mlog}\,\kappa.$$
Lean: `Formalism.L2.Indef.Tree.functional_lower_bound_of_conditions`.

**Remark 2.10.4.** The Lean name speaks of a lower bound, but the conclusion is an upper bound for the maximal slope of $R$, that is, a lower bound for the minimal slope of the dual lattice. In Lean the bound is $h_h - \mathrm{mlog}\,\kappa$ for a field $h_h$ of a numeric record, with the hypothesis $h_h = x^{C_H} b$. The proof does not use the bound $L_c \le b$ of condition 8, the nonvanishing of $z_T$ and $z_T'$ in condition 7, or any other field of the record.

**Lemma 2.10.5 (Injectivity).** Under conditions 2, 3 and 6, $\Psi$ is injective.
Lean: `Formalism.L2.Indef.Tree.psi_inj`.

*Proof.* Since $r_{ij}(\mu_0) = 1$, condition 2 at $\mu_0$ reads $\Psi \iota_{\mu_0} P_{\mu_0} = v_{\mu_0}$. Let $\Psi x = \Psi y$. As $\iota_{\mu_0}$ is bijective and $P_{\mu_0}$ surjective, $x = \iota_{\mu_0} P_{\mu_0} u$ and $y = \iota_{\mu_0} P_{\mu_0} u'$. Then $v_{\mu_0}(u - u') = 0$, so $u - u' \in U_{\mu_0} = \ker P_{\mu_0}$ by condition 3, and $x = y$. $\square$

**Lemma 2.10.6 (Local inclusion).** Put $c_w = \prod_{ij} r_{ij}(\mu(w))$, $a(w) = v_w(c_w) + d_F(w)$ and $T = T_S \cup T_f$. Then $a(w) = 0$ for $w \notin T$, and $\Psi R \subseteq \bigl(\prod_{w \in T} w^{-a(w)}\bigr) M$.
Lean: `Formalism.L2.Indef.Tree.hence_local` (also `PI.local_global_inclusion'`).

*Proof.* Fix $w$ and $t = \mu(w)$, and localize at $w$. The localization of $R$ is that of $\iota_t P_t M_t$, and $\Psi \iota_t P_t = c_w^{-1} v_t$ by condition 2. So the localization of $\Psi R$ is that of $c_w^{-1} v_t M_t$, which by condition 4 lies in $c_w^{-1} w^{-d_F(w)} M_w = w^{-a(w)} M_w$. If $w \notin T$ then $\mu(w) = \mu_0$, so $c_w = 1$, and $d_F(w) = 0$, so $a(w) = 0$. A finitely generated module lies in a lattice when it does so after localization at every finite place, which gives the global inclusion. $\square$

**Lemma 2.10.7 (Archimedean height).** If $g$ is as in condition 5, then
$$h_\infty(\Psi; X_E^\kappa, X') \le h_\infty(\Psi \iota_{\mu_0}; X_Q, X') - \mathrm{mean}_\infty g \le b_{IP}.$$
Lean: `Formalism.L2.Indef.Tree.ip_first`.

*Proof.* Fix $v$ and $q \in K^{d_Q(\mu_0)}$, and write $q = \sum_p q_p$ along the parts, which span by well-formedness. The map $\iota_{\mu_0}$ multiplies the form by $s_p = \kappa_v \prod_j \lambda_j(p, v)$ on pairs with first entry in $Q_p$, so for $X_E^\kappa$ it multiplies it by $t_p = s_p / \kappa_v$, and $t_p \ge e^{g_v}$ when $q_p \ne 0$. As the form is hermitian, $t_p \langle q_p, q_{p'} \rangle = t_{p'} \langle q_p, q_{p'} \rangle$, so writing $t_p = e^{g_v} + c_p^2$ gives $|\iota_{\mu_0} q|^2 = e^{g_v} |q|^2 + |\sum_p c_p q_p|^2 \ge e^{g_v} |q|^2$. Every vector of $K^D$ is $\iota_{\mu_0} q$, so $|\Psi \iota_{\mu_0} q| \le \|\Psi \iota_{\mu_0}\|_v e^{-g_v/2} |\iota_{\mu_0} q|$, that is $\|\Psi\|_v^2 \le \|\Psi\iota_{\mu_0}\|_v^2 e^{-g_v}$. Take logarithms and average over $v$. The second inequality is condition 5 for $V = \Psi \iota_{\mu_0}$ together with the bound on $\mathrm{mean}_\infty g$. $\square$

**Lemma 2.10.8 (Height from integrality).** Let $z \in K^\times$ and $\delta \ge 0$ with $v_w(z) \ge -3\delta_w$ for all $w$ and $\sum_F \ell_w \delta_w \le b_\delta$ for every finite $F$. Then $\sum_w \ell_w |v_w(z)| \le \mathrm{mean}_\infty \log^+ |z|_v + 6 b_\delta$.
Lean: `Formalism.AtG.norm_height_bound`.

*Proof.* Let $P$ and $Q$ be the sums of $\ell_w v_w(z)$ over the places with $v_w(z) > 0$ and of $-\ell_w v_w(z)$ over those with $v_w(z) < 0$. Then $Q \le 3 b_\delta$, and the product formula gives $P - Q = \mathrm{mean}_\infty \log |z|_v \le \mathrm{mean}_\infty \log^+ |z|_v$. Hence $P + Q \le \mathrm{mean}_\infty \log^+|z|_v + 6 b_\delta$. $\square$

*Proof of the Theorem.* Take $\Psi$ from condition 2; it is injective, and $\Psi R \subseteq (\prod_T w^{-a(w)}) M$, by the first two lemmas. Condition 4 gives $\sum_T \ell_w d_F(w) \le b_{FP}/2$, since $d_F$ vanishes on $T \setminus T_f$. The archimedean lemma gives $h_\infty(\Psi; X_E^\kappa, X') \le b_{IP}$. Put $B = \max(b_{\mathrm{arch}} + 6 b_\delta, b_{TH})$; by the height lemma and condition 7, all auxiliary elements have height at most $B$. With condition 6, the grid estimate of the volume on exponent grids bounds $\sum_T \ell_w v_w(c_w)$ by an explicit $G = m^2 \bigl(2(2 + 8N) B + 10 N b_{TH} + 2N + 6 b_\delta + 4m \Sigma_0\bigr)$, with $\Sigma_0$ a weighted sum of logarithms of prime powers. The slope inequality in the form above gives
$$\hat\mu_{\max}(R, X_E) \le -\mathrm{mlog}\,\kappa + E_M(C) + b_{IP} + 2\bigl(G + b_{FP}/2\bigr).$$
It remains to see that $E_M(C) + b_{IP} + 2G + b_{FP} \le x^{C_H} b$. This is a direct computation with the explicit constants: condition 8, with $C, x \ge 1$, $1 \le \log b$ and $\log x \le 2 \log b$, bounds each term by $b$ times a polynomial in $C, f, m, N, \log b, P(C, b)$, and the sum is at most $\mathrm{pol}(C, b)\, b \le x^{C_H} b$. $\square$

**Corollary 2.10.9 (Numeric form).** Let the scale $Z$ supply $x$ and $b$, and let the numeric record be the one built from $Z$, a constant $C_0$ and $C_H$, whose field $h_h$ is $x^{C_H} b$. Under the hypotheses of the Theorem, $\hat\mu_{\max}(R, X_E) \le x^{C_H} b - \mathrm{mlog}\,\kappa$.
Lean: `Formalism.L2.Indef.Tree.functional_lower_bound_of_conditions_numeric`.

*Proof.* The field $h_h$ of the record built from $Z$ is $x^{C_H} b$ by definition, so the Theorem applies. $\square$

**Remark 2.10.10.** The constant $C_0$ enters only three fields of the record that the conclusion does not read, so it is arbitrary.

**Remark 2.10.11 (Formalization).** The twenty numeric constants and the seventeen conditions are defined in [FunctionalLowerBoundOfConditionsNumeric.lean](lean:Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/FunctionalLowerBoundOfConditionsNumeric.lean#L98); the theorem is at line 940 and the corollary at line 1035. The lattice constant bound is passed to the theorem but never used, and the nonvanishing part of the condition on $z_T$ and $z_T'$ is discarded when it is unpacked. The slope inequality is a proposition in [ScaledCoordinatesValuationLemma.lean](lean:Formalism/LocalToGlobal/ExponentGrids/ScaledCoordinatesValuationLemma.lean#L124), proved elsewhere.

## Notes and references

The results on $U(p,q)$ feed the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/) and the segments feed [EveryCharacter](/step/every-character/). Branching, finiteness and the unfolding feed [HypsAlt is nonempty](/step/nonempty-hyps/); the polarization words feed [Theorem 5.6 of Volume 11](/entry/stmt-e-of-mp/), the Hecke algebras [the Flath factorisation](/entry/flath-factorisation-of-literature/), and the slope bound [Theorem](/entry/fun0-fit-of-leaves-alt/).

- J. E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, §24.3.
- J. C. Jantzen, *Representations of Algebraic Groups*, Part II, Chapter 2.
- R. Goodman and N. R. Wallach, *Symmetry, Representations, and Invariants*, Chapter 8.
- I. M. Gelfand and M. L. Tsetlin, *Finite-dimensional representations of the group of unimodular matrices*, Doklady Akad. Nauk SSSR 71 (1950).
- R. Howe and T. Umeda, *The Capelli identity, the double commutant theorem, and multiplicity-free actions*, Math. Ann. 290 (1991), §1.
- C. De Concini, D. Eisenbud and C. Procesi, *Young diagrams and determinantal varieties*, Invent. Math. 56 (1980), §1.
- W. Casselman and M. S. Osborne, *The n-cohomology of representations with an infinitesimal character*, Compositio Math. 31 (1975), §2.
- H. Hecht and W. Schmid, *A proof of Blattner's conjecture*, Invent. Math. 31 (1975), §1.
- Harish-Chandra, *Discrete series for semisimple Lie groups II*, Acta Math. 116 (1966), §7.
- Harish-Chandra, *Automorphic Forms on Semisimple Lie Groups*, Lecture Notes in Math. 62 (1968), Chapter I.
- C. Moeglin and J.-L. Waldspurger, *Spectral Decomposition and Eisenstein Series*, Chapter I.
- D. Flath, *Decomposition of representations into tensor products*, Proc. Sympos. Pure Math. 33, Part 1 (1979), §2.
- I. N. Bernstein, *All reductive p-adic groups are tame*, Funct. Anal. Appl. 8 (1974), §1.
- A. S. Amitsur and J. Levitzki, *Minimal identities for algebras*, Proc. Amer. Math. Soc. 1 (1950), §1.
- F. Bruhat and J. Tits, *Groupes réductifs sur un corps local I*, Publ. Math. IHÉS 41 (1972), §4.4.
- I. N. Bernstein and A. V. Zelevinsky, *Induced representations of reductive p-adic groups I*, Ann. Sci. ÉNS 10 (1977), §2 and §4.
- A. V. Zelevinsky, *Induced representations of reductive p-adic groups II*, Ann. Sci. ÉNS 13 (1980), §3.
- J.-B. Bost, *Périodes et isogénies des variétés abéliennes sur les corps de nombres*, Séminaire Bourbaki Exp. 795, Astérisque 237 (1996), §4.
