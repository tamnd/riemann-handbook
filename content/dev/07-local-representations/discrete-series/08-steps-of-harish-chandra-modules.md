---
title: Steps of Harish-Chandra modules
decls:
  - CompanionTheory.RgExh.Hk.UnitB.unit_of_dualFacts
  - CompanionTheory.RgExh.Hk.unitarity
  - CompanionTheory.RgExh.Hk.hecke_algebra_exhaustion
  - CompanionTheory.RgExh.U.far_regular_exhaustion
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Steps of Harish-Chandra modules

The classification of the discrete series of $U(p,q)$ in the next section moves a Harish-Chandra module along a path of steps. A step tensors the module with the standard representation $\mathbb{C}^n$ and keeps one generalized eigenspace of a Casimir type operator. This section proves three algebraic facts about steps. First, a step can be undone by the dual step. Second, along a path of steps whose end has a scalar character, the end is simple and fixes the start up to isomorphism. Third, a unitary module whose character has entries that are far apart contains a lowest $K$-type of discrete series type. All three are inputs of [Theorem 3.9.14](/entry/ds-exhaust/), which the step [EveryCharacter from the literature](/step/every-character-of-literature/) uses.

Background: [admissible representations and $(\mathfrak{g}, K)$-modules](/learn/real-groups/#admissible-representations-and-mathfrakg-k-modules), [highest weights](/learn/representations/#highest-weights-and-branching), [[Harish-Chandra module|2MKHH636C3]].

### Modules, characters and steps

**Definition 3.8.1 ($\mathfrak{gl}_n$-module).** A *$\mathfrak{gl}_n$-module* $X$ is a complex vector space $V$ with linear operators $E_{ab}$, $1 \leq a, b \leq n$, such that
$$E_{ab}E_{cd} - E_{cd}E_{ab} = \delta_{bc}E_{ad} - \delta_{da}E_{cb}.$$
An *isomorphism* $X \cong X'$ is a linear bijection $\phi$ with $\phi E_{ab} = E'_{ab}\phi$ for all $a, b$. The module is *simple* if $V \neq 0$ and the only subspaces stable under all $E_{ab}$ are $0$ and $V$.

Put $c_n = (n-1)/2$ and, for $\chi \in \mathbb{C}^n$, $P_\chi(Y) = \prod_{s}(Y + \chi_s)$. Let $T(u)_{ab} = u\,\delta_{ab} + E_{ab}$. The *quantum determinant* is the ordered sum
$$\operatorname{qdet}(u) = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\, T(u)_{\sigma(1)1}\, T(u-1)_{\sigma(2)2} \cdots T(u-n+1)_{\sigma(n)n}.$$

**Definition 3.8.2 (Character).** The module $X$ has *character* $\chi \in \mathbb{C}^n$ if there is $k \geq 0$ such that $\bigl(\operatorname{qdet}(Y + c_n) - P_\chi(Y)\bigr)^k = 0$ for every $Y \in \mathbb{C}$. It has *scalar character* $\chi$ if $\operatorname{qdet}(Y + c_n) = P_\chi(Y)$ for every $Y$.

The tensor product with the standard representation is $V^n$ with $(E^{\otimes}_{ab}u)_i = E_{ab}u_i + \delta_{ia}u_b$. The tensor product with the dual representation is $V^n$ with $(E^{\vee}_{ab}u)_i = E_{ab}u_i - \delta_{ib}u_a$. Put
$$(\Omega u)_b = \sum_a E_{ab}u_a, \qquad (\Omega^\vee u)_a = -\sum_b E_{ab}u_b.$$
The operator $\Omega$ commutes with all $E^{\otimes}_{ab}$.

**Definition 3.8.3 (Step and back step).** For $z \in \mathbb{C}$, the *step* $\operatorname{st}(X, z)$ is the submodule of $V^n$ (with the operators $E^{\otimes}$) given by the generalized eigenspace of $\Omega$ for the eigenvalue $z - c_n$. The *back space* $B(X, z)$ is the generalized eigenspace of $\Omega^\vee$ for the eigenvalue $-z - c_n$. If $B(X, z)$ is stable under all $E^{\vee}_{ab}$, the *back step* $\operatorname{bk}(X, z)$ is $B(X, z)$ with these operators. We say that *back spaces are stable* if this holds for all $n$, $X$ and $z$.

**Definition 3.8.4 (Dual facts).** We say that the *dual facts* hold if for every $n$, every $X$ and every character $\chi$ of $X$:

1. there is $K$ with $\prod_t \bigl(\Omega^\vee + \chi_t + c_n\bigr)^K = 0$ on $V^n$;
2. for every $s$ such that $B(X, \chi_s)$ is stable, $\operatorname{bk}(X, \chi_s)$ has character $\chi - e_s$;
3. for every $s$, if $V \neq 0$ and $\chi_r \neq \chi_s - 1$ for all $r$, then $B(X, \chi_s) \neq 0$.

### The back step undoes the step

**Theorem 3.8.5 (The back step undoes the step).** Assume that the dual facts hold. Let $X$ be a $\mathfrak{gl}_n$-module with scalar character $\chi$, and let $s$ be an index. Assume that back spaces are stable, that $\chi_r \neq \chi_s + 1$ for all $r$, that $\chi_r \neq \chi_s$ for all $r \neq s$, and that $\Omega f = (\chi_s - c_n)f$ for every $f$ in $\operatorname{st}(X, \chi_s)$. Then
$$\operatorname{bk}\bigl(\operatorname{st}(X, \chi_s), \chi_s + 1\bigr) \cong X.$$

Lean: `CompanionTheory.RgExh.Hk.UnitB.unit_of_dualFacts`

*Proof.* For $n = 0$ there is no index $s$. Let $n \geq 1$. A scalar character is a character with $k = 1$, so the first dual fact gives $K$ with $\prod_t(\Omega^\vee + \chi_t + c_n)^K = 0$.

Put $\kappa = \prod_{t \neq s}(\chi_t - \chi_s)$, which is not $0$ because $\chi_t \neq \chi_s$ for $t \neq s$. Let $P = \kappa^{-1}\operatorname{qdet}^{\otimes}(c_n - \chi_s)$, where $\operatorname{qdet}^{\otimes}$ is the quantum determinant of the operators $E^{\otimes}_{ab}$. Three identities for quantum determinants of a tensor product with $\mathbb{C}^n$ give the following properties of $P$: $\Omega P = (\chi_s - c_n)P$, so $P$ maps $V^n$ into $\operatorname{st}(X, \chi_s)$; $Pf = f$ if $\Omega f = (\chi_s - c_n)f$; and $P$ commutes with $\Omega$ and with every $E^{\otimes}_{ab}$, because the quantum determinant is central. A fourth identity, the sum of the principal minors, gives
$$\sum_c \bigl(P(e_c v)\bigr)_c = \kappa^{-1}\bigl(-P_\chi(-\chi_s - 1)\bigr)\, v,$$
where $e_c v \in V^n$ has $v$ in place $c$ and $0$ elsewhere.

Let $Y = \operatorname{st}(X, \chi_s)$ and define $\varphi : V \to Y^n$ by $\varphi(v)_c = P(e_c v)$. A direct computation with $\sum_c E^{\otimes}_{ac}(e_c v) = \Omega(e_a v) + n\, e_a v$ shows that $\varphi(v)$ is an eigenvector of the operator $\Omega^\vee$ of $Y$ for the eigenvalue $-(\chi_s + 1) - c_n$. So $\varphi$ maps into $B(Y, \chi_s + 1)$. Since $P$ commutes with the $E^{\otimes}_{ab}$, the map $\varphi$ carries $E_{ab}$ to the dual tensor operator $E^{\vee}_{ab}$ of $Y$.

The map $\varphi$ is injective. If $\varphi(v) = 0$, the trace identity gives $\kappa^{-1}(-P_\chi(-\chi_s - 1))v = 0$. Here $P_\chi(-\chi_s - 1) = \prod_t(\chi_t - \chi_s - 1) \neq 0$ because $\chi_t \neq \chi_s + 1$. So $v = 0$.

The map $\varphi$ is surjective. Write an element $G$ of $B(Y, \chi_s + 1)$ as a matrix $H = (H_{cd})$ of vectors of $V$, with column $H_c = G_c \in V^n$. On such matrices let $Y_1$ apply $\Omega$ to each column, let $Y_2$ be the operator $\Omega^\vee$ of $Y$, let $\eta(v)$ be the matrix with columns $e_c v$, and let $\psi(H) = \sum_c H_{cc}$. Let $I$ be the span of all $Y_1^k\eta(v)$. Let $\Omega'$ apply $\Omega^\vee$ of $X$ to the first index of $H$. Then $\Omega' = Y_2 + \eta\circ\psi$, and $I$ is stable under $Y_2$ and $\Omega'$. Put $\beta = -(\chi_s + 1) - c_n$. By induction on $k$, $(\Omega' - \beta)^k H - (Y_2 - \beta)^k H \in I$. Since $G$ is in the generalized eigenspace, $(Y_2 - \beta)^k H = 0$ for some $k$, so $(\Omega' - \beta)^k H \in I$. The polynomials
$$p(x) = \prod_t (x + \chi_t + c_n)^K \quad\text{and}\quad q(x) = (x - \beta)^k$$
are coprime, because $-\chi_t - c_n = \beta$ would give $\chi_t = \chi_s + 1$. Choose $A$ and $B$ with $Ap + Bq = 1$. The relation $p(\Omega^\vee) = 0$ on $V^n$ gives $p(\Omega') = 0$. So
$$H = A(\Omega')p(\Omega')H + B(\Omega')q(\Omega')H = B(\Omega')(\Omega' - \beta)^k H \in I.$$
For $H = Y_1^k\eta(v)$ we have $P(H_c) = (\chi_s - c_n)^k P(e_c v)$, so by linearity there is $v \in V$ with $P(H_c) = P(e_c v)$ for all $c$ and all $H \in I$. Each column $H_c$ lies in $Y$, on which $\Omega$ acts by $\chi_s - c_n$, so $P(H_c) = H_c$. Hence $G = \varphi(v)$.

So $\varphi$ is a linear bijection that intertwines the operators, and its inverse is the isomorphism of the claim. $\square$

**Theorem 3.8.6 (Back step isomorphism).** The conclusion of the previous theorem holds without the assumption on the dual facts: for every $X$, $\chi$ and $s$ as there, $\operatorname{bk}(\operatorname{st}(X, \chi_s), \chi_s + 1) \cong X$.

Lean: `CompanionTheory.RgExh.Hk.unitarity`

*Proof.* The dual facts hold: this is a separate theorem, which derives them from four statements: the quantum determinant of the module twisted by $E_{ab} \mapsto -E_{ba}$ is $(-1)^n\operatorname{qdet}(-u + n - 1)$, the Cayley-Hamilton identity $\prod_t(\Omega - \chi_t + c_n)^K = 0$, the shift of characters under a step, and the nonvanishing of steps. Apply [Theorem 3.8.5](/entry/unit-of-dual-facts/). $\square$

### Paths of steps

For $\chi \in \mathbb{C}^n$ and a list $s_1, \dots, s_k$ of indices, the *path* starts at $(X, \chi)$ and replaces $(X, \chi)$ by $(\operatorname{st}(X, \chi_{s_1}), \chi + e_{s_1})$, then repeats with $s_2$, and so on. Let $\operatorname{path}(X)$ and $\operatorname{end}(\chi)$ be the final pair. The path is *good* if at each stage $\chi_r \neq \chi_{s} + 1$ for all $r$, where $\chi$ is the current label and $s$ the next index. The path is *simple* if at each stage $\chi_r \neq \chi_s$ for all $r \neq s$.

**Theorem 3.8.7 (Paths of steps).** Let $X$ be a simple $\mathfrak{gl}_n$-module with character $\chi$, and let a good path for $\chi$ be given. If $\operatorname{path}(X)$ has scalar character $\operatorname{end}(\chi)$, then:

1. the path is simple;
2. $\operatorname{path}(X)$ is simple;
3. for every simple $X'$ with character $\chi$, if $\operatorname{path}(X) \cong \operatorname{path}(X')$, then $X \cong X'$.

Lean: `CompanionTheory.RgExh.Hk.hecke_algebra_exhaustion`

*Proof.* The proof uses these facts on one step from $(X, \chi)$ in direction $s$, with $\chi_r \neq \chi_s + 1$ for all $r$:

- (shift) if $X$ has character $\chi$, the step has character $\chi + e_s$;
- (nonvanishing) if also $V \neq 0$, the step is not $0$;
- (backward) if $X$ has character $\chi$ and the step has scalar character $\chi + e_s$, then $X$ has scalar character $\chi$ and $\Omega$ acts on the step by the scalar $\chi_s - c_n$;
- (nonscalar) if $X$ has scalar character $\chi$, $V \neq 0$, and $\chi_r = \chi_s$ for some $r \neq s$, then $\Omega$ is not the scalar $\chi_s - c_n$ on the step;
- (scalar) if $X$ has scalar character $\chi$ and $\chi_r \neq \chi_s$ for $r \neq s$, then $\Omega$ is the scalar $\chi_s - c_n$ on the step;
- (forward) if also $X$ is simple, the step is simple;
- (reflection) if $X$ and $X'$ have scalar character $\chi$, $\chi_r \neq \chi_s$ for $r \neq s$, and the steps of $X$ and $X'$ are isomorphic, then $X \cong X'$.

Also a simple module with character $\chi$ has scalar character $\chi$: the operator $N = \operatorname{qdet}(Y + c_n) - P_\chi(Y)$ commutes with all $E_{ab}$, so its kernel is a stable subspace; it is not $0$ because $N^k = 0$ and $V \neq 0$, so it is $V$.

Backward pass, by induction on the length of the path. The shift and nonvanishing facts carry "character $\chi$ and $V \neq 0$" one step forward. By induction the step from $X$ has scalar character $\chi + e_s$ and the rest of the path is simple. The backward fact gives that $X$ has scalar character $\chi$ and that $\Omega$ is scalar on the step. If $\chi_r = \chi_s$ for some $r \neq s$, the nonscalar fact would contradict this. So the first stage is simple, and the path is simple.

Forward pass, by induction again. Since $X$ is simple, it has scalar character $\chi$. The scalar fact and the forward fact show that the step is simple, and the shift fact gives its character. By induction $\operatorname{path}(X)$ is simple. For $X'$ simple with character $\chi$, the same argument applies to $X'$. If $\operatorname{path}(X) \cong \operatorname{path}(X')$, the induction gives an isomorphism of the first steps, and the reflection fact gives $X \cong X'$. $\square$

The forward fact and the reflection fact are proved from [Theorem 3.8.6](/entry/unitarity/) together with the identities for quantum determinants used above.

### Far regular characters

A $\mathfrak{gl}_n$-module on an inner product space is *unitary* for the sign vector $\varepsilon$ if $\langle E_{ab}x, y\rangle = \operatorname{sgn}_\varepsilon(a,b)\langle x, E_{ba}y\rangle$, where $\operatorname{sgn}_\varepsilon(a,b)$ is $1$ if $\varepsilon_a = \varepsilon_b$ and $-1$ otherwise. It is *locally $K$-finite* if every vector lies in a finite dimensional subspace that is stable under all $E_{ab}$ with $\varepsilon_a = \varepsilon_b$. It has *integral weights* if every nonzero $x$ with $E_{aa}x = \mu_a x$ for all $a$ has $\mu \in \mathbb{Z}^n$. A vector $w$ is *$K$-highest of weight $\mu$* if $E_{aa}w = \mu_a w$ for all $a$ and $E_{ab}w = 0$ for $a < b$ with $\varepsilon_a = \varepsilon_b$.

Let $\rho_c(a) = \frac12(\#\{b > a : \varepsilon_b = \varepsilon_a\} - \#\{b < a : \varepsilon_b = \varepsilon_a\})$, and let $\rho_n(a)$ be the same expression with $\varepsilon_b \neq \varepsilon_a$. A *Harish-Chandra parameter* is a strictly decreasing $\mu \in \mathbb{R}^n$ with $\mu_a - c_n \in \mathbb{Z}$ for all $a$. Put $\Lambda(\mu) = \mu + \rho_n - \rho_c$ and $\|\nu\|_c = \|\nu + 2\rho_c\|$.

**Definition 3.8.8 (Algebraic discrete series).** Let $\sigma$ be a permutation of $\{1, \dots, n\}$, and write $X^\sigma$ for the module with operators $E_{\sigma(a)\sigma(b)}$ and sign vector $\varepsilon \circ \sigma$. The module $X$ is an *algebraic discrete series* with data $(\sigma, \mu)$ if $\mu$ is a Harish-Chandra parameter, $\sigma(a) < \sigma(b)$ whenever $a < b$ and $\varepsilon_{\sigma(a)} = \varepsilon_{\sigma(b)}$, the module $X^\sigma$ has a nonzero $K$-highest vector of weight $\Lambda(\mu)$, and $\|\Lambda(\mu)\|_c \leq \|\nu\|_c$ for every weight $\nu$ of a nonzero $K$-highest vector of $X^\sigma$.

**Theorem 3.8.9 (Far regular characters).** For every $n$, every $C$ and every $\delta > 0$ there is $N_0$ with the following property. Let $\varepsilon$ be a sign vector, and let $X$ be a nonzero $\mathfrak{gl}_n$-module on an inner product space that is unitary for $\varepsilon$, locally $K$-finite, with integral weights and with scalar character $\chi$. Let $N \geq N_0$, and assume that
$$|\operatorname{Re}\chi_a - \operatorname{Re}\chi_b| \geq \delta N \ (a \neq b), \qquad |\operatorname{Re}\chi_a| \leq CN, \qquad |\operatorname{Im}\chi_a| \leq C.$$
Then $X$ is an algebraic discrete series with some data $(\sigma, \mu)$.

Lean: `CompanionTheory.RgExh.U.far_regular_exhaustion`

*Proof.* The theorem is derived from five statements, which we list without proof. (i) Every nonzero unitary, locally $K$-finite module with integral weights has a nonzero $K$-highest vector whose integral weight $\gamma$ is minimal for $\|\cdot\|_c$. (ii) Renumbering by an order preserving $\sigma$ keeps unitarity, local finiteness, scalar characters and $K$-highest vectors. (iii) There is $K_n$ such that for a unitary module with scalar character $\chi$ and a nonzero $K$-highest vector of weight $\gamma$,
$$\sum_a \bigl((\operatorname{Re}\chi_a)^2 - (\operatorname{Im}\chi_a)^2\bigr) \leq \|\gamma + \rho_c\|^2 + K_n.$$
(iv) A block statement: if the minimal weight $\gamma$ has gaps between levels, the sums of $\chi$ over each level are within a bound of the corresponding sums built from $\gamma$. (v) A numerical statement: under the bounds of (iii) and (iv) and the hypotheses on $\chi$, for $N \geq N_0$ the levels are pairwise distinct. A further argument, which we did not open, combines (i) to (v) and gives $\sigma$ and $\mu$. $\square$

**Remark 3.8.10 (Formalization).** The statement called "unitarity" is the back step isomorphism, not a statement on inner products. There is a second theorem with the same name and statement outside any namespace ([Unitarity.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/HeckeAlgebraActions/HeckeUnits/Unitarity.lean#L145)). Stability of back spaces is a hypothesis inside the statement, not a conclusion. The proof of the theorem on paths takes the Cayley-Hamilton identity as an argument but does not use it ([ScalCharOfSimple.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/HeckeAlgebraActions/ScalarCharacters/ScalCharOfSimple.lean#L106)). The rank one, $\Omega$-minor, tensor and principal minor identities for quantum determinants, the dual facts, the forward and reflection facts, and the five inputs of the last theorem enter as statements; we did not open their proofs. For the last theorem we read only the statements of the inputs, not the proof that combines them.
