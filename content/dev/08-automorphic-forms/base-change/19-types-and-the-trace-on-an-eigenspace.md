---
title: Types and the trace on an eigenspace
decls:
  - UpperTheory.ConvolutionTheory.T.inertData
  - UpperTheory.ConvolutionTheory.T.tyEx
  - UpperTheory.ConvolutionTheory.C.termEV
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Types and the trace on an eigenspace

The [twisted trace identity](/entry/g-core/) compares a twisted trace at one non-split place $v$ with an ordinary trace below it. Its proof isolates one automorphic representation by test functions that are characteristic functions of types, and then computes the twisted trace of a Hecke operator on an eigenspace of that representation as a product of local traces. This section gives the three inputs: types at a non-split place, a global datum of types, and the product formula for the trace.

Throughout, $F$ and $E$ are totally complex number fields, $E/F$ is Galois of prime degree $\ell$, $\sigma$ generates $\mathrm{Gal}(E/F)$, and $n > 0$. Let $L^2$ be the space of square integrable functions on the norm-one quotient of $\mathrm{GL}_n$ over $E$, with a Haar measure $\mu$ and the right action $R$. Let $V \subseteq L^2$ be a summand of the cuspidal part of $L^2$. For a place $w$ of $E$ we write $G_w = \mathrm{GL}_n(E_w)$, and for a place $v$ of $F$ we write $G_v = \mathrm{GL}_n(F_v)$.

**Definition 7.19.1 (Type and eigenspace).** A type at $w$ is a pair $(J, \chi)$ of a compact open subgroup $J \subseteq G_w$ and a locally constant function $\chi$ on $G_w$ whose restriction to $J$ is a unitary character. The eigenspace $L^2(J, \chi)$ is the set of $f \in L^2$ with $R(x)f = \chi(x)f$ for all $x \in J$. We say that $V$ has rank one at $(J, \chi)$ if for every $g \in G_w$ there is $c \in \mathbb{C}$ with $\mathrm{pr}(R(g)f) = cf$ for all $f \in V \cap L^2(J, \chi)$, where $\mathrm{pr}$ is the orthogonal projection onto $L^2(J, \chi)$.

If the local component of $V$ at $w$ contains the type $(J, \chi)$ with multiplicity one, then $V$ has rank one at $(J, \chi)$. The function $\bar\chi\,\mathbf{1}_J$ acts on $V$ as a multiple of the projection onto $V \cap L^2(J, \chi)$, so it detects the type.

We use [matching with a constant](/entry/deep-hecke/) of a function on $\mathrm{GL}_n(E \otimes_F F_v)$ with a function on $G_v$, as in the local matching of this chapter. A test function is a locally constant function with compact support.

**Theorem 7.19.2 (Types at a non-split place).** Let $V$ be a summand of the cuspidal spectrum and $v$ a finite place of $F$ that does not split in $E$, and let $w$ be the place above $v$. There are a type $(J, \chi)$ at $w$, a test function $f$ on $G_v$, an open subgroup $U_E$ of the unit set of $\mathrm{GL}_n(E \otimes F_v)$ and an open subgroup $U_F \subseteq \mathrm{GL}_n(\mathcal{O}_v)$ with the following properties.

1. $V$ has rank one at $(J, \chi)$ and $V \cap L^2(J, \chi) \ne 0$.
2. $J$ is stable under $\sigma$, and $\chi(\sigma x) = \chi(x)$ for $x \in J$.
3. The test function $\varphi = \bar\chi\,\mathbf{1}_J$ matches $f$ with constant 1.
4. $\varphi(yg) = \varphi(g)$ for $y \in U_E$ and $f(yg) = f(g)$ for $y \in U_F$.

Lean: `UpperTheory.ConvolutionTheory.T.inertData`.

*Proof.* Since $\ell$ is prime and $v$ does not split, $w$ is the only place above $v$. We use two local facts. First, there is a radius $\rho > 0$ such that every test function on $G_w$ supported in the ball of radius $\rho$ about $1$ matches some test function on $G_v$ with constant 1; this is matching near the identity, where the norm map is a local homeomorphism on regular elements. Second, in every neighbourhood of $1$ there is a type $(J, \chi)$ with properties 1 and 2; this is the existence of types of Howe for the local component of $V$. Take such a type inside the ball of radius $\rho$. Then $\varphi = \bar\chi\,\mathbf{1}_J$ is a test function supported in the ball, and the first fact gives $f$. Each test function is left invariant under some open compact subgroup, which gives $U_E$ and $U_F$. $\square$

**Definition 7.19.3 (Type datum).** Fix a finite place $q$ of $F$ that splits in $E$ and a place $w_0$ above $q$. A type datum consists of a finite set $S$ of finite places of $F$ with $q \notin S$, a type $(J_w, \chi_w)$ at every finite place $w$ of $E$, and a chosen place $w_v$ above each $v$, such that:

1. if $w$ lies over $v \notin S \cup \{q\}$, then $J_w = \mathrm{GL}_n(\mathcal{O}_w)$ and $\chi_w = 1$;
2. if $w$ lies over $q$, then $J_w$ is the Iwahori subgroup;
3. if $w$ lies over a split place, then $\chi_w = 1$;
4. for each $v$, the group $\prod_{w \mid v} J_w$ is stable under $\sigma$, and $\prod_{w \mid v}\chi_w$ is $\sigma$-invariant on it.

The typed space is the intersection of the eigenspaces $L^2(J_w, \chi_w)$ over all $w$. Local data $L$ fit a type datum and a family $\psi = (\psi_v)$ of test functions on $G_{w_v}$ if: $L$ has the set $S$; at a split $v \in S$, $\psi_v$ is bi-invariant under $J_{w_v}$, and the function of $L$ at $v$ is $\psi_v$ at $w_v$ tensored with $\mathbf{1}_{J_w}$ at the other places above $v$; at a non-split $v \in S$, the function of $L$ at $v$ is $\psi_v$.

The local data of a trace formula comparison are the functions $\varphi_v$ on $\mathrm{GL}_n(E \otimes F_v)$ and $f_v$ on $G_v$ for $v \in S$, with matching constants $c_v$ and open subgroups of invariance, together with the Iwahori functions at $q$ and the unit functions outside $S \cup \{q\}$.

**Theorem 7.19.4 (Existence of a type datum).** Let $V$ be a summand of the cuspidal spectrum. Let $q$ split in $E$ with $w_0$ above it, and let $S$ be a finite set of finite places with $q \notin S$, such that $E/F$ is unramified outside $S$ and $V$ has nonzero $\mathrm{GL}_n(\mathcal{O}_w)$-fixed vectors for every $w$ not above $S$. Choose a place $w_v$ above each $v$. Then there is a type datum $T$ with the set $S$ and the chosen places $w_v$, with the following properties.

1. $V$ meets the typed space of $T$ in a nonzero vector.
2. At each non-split $v \in S$ and each $w \mid v$, $V$ has rank one at $(J_w, \chi_w)$.
3. There are constants $c_v$, test functions $f_v$ and open subgroups $U_v$ of $G_v$ such that for every family $\psi$ of test functions at the split places of $S$, bi-invariant under $J_{w_v}$, there are local data $L$ that fit $T$ and $\psi$, with constants $c_v$ and subgroups $U_v$ at $v \in S$, with the function $\psi_v$ on $G_v \cong G_{w_v}$ at a split $v$, and with $f_v$ at a non-split $v$.

Lean: `UpperTheory.ConvolutionTheory.T.tyEx`.

*Proof.* We choose the type place by place. At a split $v \in S$ we take a compact open $U \subseteq \mathrm{GL}_n(\mathcal{O}_v)$ whose images $J_w$ at the places $w \mid v$ have nonzero fixed vectors in $V$, with $\chi_w = 1$. These groups are stable under $\sigma$, which permutes the places above $v$, and the function $\psi_v$ at $w_v$ tensored with $\mathbf{1}_{J_w}$ at the other places matches $\psi_v$ with a constant that does not depend on $\psi_v$. At a non-split $v \in S$ we take the type of the [theorem on types at a non-split place](/entry/inert-data/). At $q$ we take Iwahori subgroups, and outside $S \cup \{q\}$ the maximal compact subgroups; both are stable under $\sigma$. Finally, a vector that lies in each local eigenspace can be found in $V$, because $V$ is a restricted tensor product of its local components. $\square$

The trace that the comparison needs is taken on an eigenspace of an archimedean operator. We fix the archimedean data of the comparison: the twist operator $\theta$ on $L^2$ induced by $\sigma$, Haar measures on the archimedean groups, archimedean test functions $a_E$ over $E$ and $a$ over $F$, and continuous homomorphisms $s_0, \dots, s_{\ell - 1}$ from the archimedean group over $F$ to that over $E$. For $y > 0$ let $Z(y)$ be the typed vectors $f \in V$ with $O_i f = yf$ for the operators $O_i$ obtained from $a$ and $s_i$.

For local data $L$ and a dominant $e \in \mathbb{Z}^n$, a side datum is a test function $g_L$ on $\mathrm{GL}_n(\mathbb{A}_E)$ whose archimedean part is $a_E$ and whose finite part is the product of the functions of $L$, an operator $A$ given by the right action of an archimedean test function, and the Iwahori Hecke operator $U(e)$ at $w_0$ with exponent $e$.

**Theorem 7.19.5 (Trace on an eigenspace).** Assume that $\theta V = V$ and let $T$ be a type datum such that, at each non-split $v \in S$ and $w \mid v$, $V$ has rank one at $(J_w, \chi_w)$ and $V \cap L^2(J_w, \chi_w) \ne 0$. Let $\tau_0$ be a representation of $G_{w_0}$ that occurs in $V$ at $w_0$, and for $v \in S$ let $\tau_v$ occur in $V$ at $w_v$. For a non-split $v \in S$, let $g_v$ be the local Galois action on $G_{w_v}$ and $I_v$ an operator with $I_v\tau_v(x) = \tau_v(g_vx)I_v$. Let $y > 0$. Then there is $c \in \mathbb{C}$, nonzero if $Z(y) \ne 0$, with the following property. Let $L$ fit $T$ and $\psi$, let $e$ be dominant and take a side datum $(g_L, A, U(e))$. Let $j \in \mathbb{N}$, let $s_q$ be the trace of the characteristic function of $I\varpi^{je}I$ on $\tau_0$, let $t_v$ be the trace of $\psi_v$ on $\tau_v$ for split $v \in S$, and the twisted trace of $\psi_v$ on $(\tau_v, I_v)$ for non-split $v \in S$. Then
$$\begin{aligned} &\mathrm{tr}\big(U(e)^j \circ R(g_L) \circ \theta \,\big|\, V_A(y^{\ell})\big) \\ &\qquad = c\, s_q \prod_{v \in S} t_v, \end{aligned}$$
where $V_A(y^{\ell})$ is the eigenspace of $A$ in $V$ for the eigenvalue $y^{\ell}$.

Lean: `UpperTheory.ConvolutionTheory.C.termEV`.

*Proof.* The eigenspace $V_A(y^{\ell})$, cut down by the fixed vectors at the places outside $S$, is finite dimensional. The operator factors as a tensor product of local operators. At $w_0$, $U(e)^j$ acts through the local component $\tau_0$, and its contribution is $s_q$. At a split $v \in S$, $R(\psi_v)$ acts on the $J_{w_v}$-fixed part of the local component, with trace $t_v$. At a non-split $v \in S$, the rank one condition gives a unique eigenline, and the composite of $R(\psi_v)$ with the twist acts on it through the twisted trace $t_v$. At the archimedean places, the twist $\theta$ commutes with the archimedean operators and with the projection to the typed space, and the archimedean base change trace comparison gives a factor $c_1 \ne 0$; a second factor $c_0$ comes from the eigenvalue $y^{\ell}$ of the twisted archimedean operator. The constant $c$ is built from these factors, and it is nonzero when $Z(y) \ne 0$. $\square$

**Remark 7.19.6 (Formalization).** `inertData` is at [InertData.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/TraceSplitting/InertData.lean#L48); its two local facts are `atDown` and `howeType`, which we did not unfold. In the proof of `tyEx` the last step is `typedEx`, which we did not unfold either. `tyEx` is the term `tyEx_of splitLev splitStable splitMatch inertData offStable L1.typedEx L1.eigBasic` ([TyEx.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/TraceSplitting/TyEx.lean#L10)); the statement `TyEx` is in NormCharSplit.lean:118. `termEV` is at [TermEV.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/PowerSumTraces/TermEV.lean#L232), runs to line 492 with `maxHeartbeats 3200000`, and calls `twistY`, `archimedean_baseChange_trace_comparison`, `finiteDimensional_eigenspace_inf_fixed_offN_CMDatum`, `twistFactor` and `eigenspace_factorization_over_nonsplit_places_CMDatum`; we did not unfold these, so the proof above is an outline of their roles. We also did not unfold the archimedean predicates `IsBlockElement` and `ArchSlot`, or the notion of a summand, `IsSummandOf`. The constant $c$ in `termEV` is asserted to be nonzero only under $Z(y) \ne 0$, where $Z(y)$ is `T.Z`; the statement also makes no claim on the dimension of $V_A(y^\ell)$. The statement `TermEV` writes the degree as $k + 1$ with $k + 1$ prime and the eigenvalue as $y^{k + 1}$, and, unlike `TyEx` and `InertData`, it does not assume that $F$ and $E$ are totally complex.
