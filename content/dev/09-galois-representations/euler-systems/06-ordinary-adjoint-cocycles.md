---
title: Ordinary adjoint cocycles
decls:
  - UpperTheory.V.Th.b1absO
  - UpperTheory.V.Th.b1O
  - UpperTheory.V.Th.hidaX
  - UpperTheory.V.Th.ordVan2
  - UpperTheory.V.Th.core
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Ordinary adjoint cocycles

This section proves that an ordinary cocycle of the adjoint of an automorphic [[Galois representation|JQEYEQJY2G]] of dimension 2 to 4 is a coboundary. This is the statement that the [window bound](/proof/vwin/) calls the core. There are two inputs. The first is a bound for the traces of Selmer classes at Taylor-Wiles levels, from a Greenberg-Wiles count. The second is a Hecke ideal that vanishes at every automorphic point. With these inputs [the core argument](/entry/core-o-of-literal-automorphy-n/) shows that a derivation of the universal ordinary ring kills all traces. This section gives the reduction to that argument. The background is in [continuous cohomology](/learn/galois-cohomology/#continuous-cohomology), [Selmer groups](/learn/galois-cohomology/#selmer-and-tate-shafarevich-groups) and [Hida theory](/learn/galois-cohomology/#hida-theory).

### Selmer bounds at Taylor-Wiles levels

Fix an odd prime $\ell$ and a coefficient ring $\mathcal{O}$: a discrete valuation ring that is a $\mathbb{Z}_\ell$-algebra with residue field $k$ of characteristic $\ell$. Write $\mathcal{O}_m = \mathcal{O}/\mathfrak{m}^m$ and $\mathrm{ad}_m(g) Z = \rho_m(g) Z \rho_m(g)^{-1}$.

A *Galois frame* is a profinite group $\Gamma$ with a character $\eta \colon \Gamma \to \{\pm 1\}$, its kernel $G_0$, a [[cyclotomic character|XSGB5K2KEG]] $\varepsilon \colon \Gamma \to \mathbb{Z}_\ell^\times$, a complex conjugation $c$, decomposition groups $G_v \to G_0$ at the places $v \mid \ell$ and inertia groups $I_u$ at a finite set of other places. We do not unfold the full structure.

**Definition 5.6.1.** A *point* of dimension $n$ over $\mathcal{O}$ is a continuous homomorphism $\rho \colon G_0 \to \mathrm{GL}_n(\mathcal{O})$ with:

1. a matrix $P$ with $P^T = \pm P$ such that $\rho$ is polarized by $P$;
2. a nonzero $a \in \mathcal{O}$ with $a M_n(\mathcal{O}) \subseteq \mathrm{span}_{\mathcal{O}}\, \rho(G_0)$;
3. $\rho = 1$ on each $I_u$;
4. at each $v \mid \ell$ a matrix $w_v$ such that $w_v^{-1} \rho w_v$ is upper triangular on $G_v$ with diagonal characters $\psi_{v,1}, \ldots, \psi_{v,n}$, with $\psi_{v,i} \neq \psi_{v,j}\, \varepsilon$ for $i < j$, and with the $\psi_{v,i}(g)$ distinct at some $g$.

**Definition 5.6.2.** Let $h \colon \Gamma_N \to \Gamma$ be a map of frames. The *Selmer set* $\mathrm{Sel}_m$ is the set of locally constant $z \colon G_{N,0} \to M_n(\mathcal{O}_m)$ with $z(gg') = z(g) + \mathrm{ad}_m(g) z(g')$, $P z(cgc^{-1}) = -z(g)^T P$, $z = 0$ on each $I_u$, and the ordinary local condition at each $v \mid \ell$. The *trace* of $z$ is the function $g \mapsto \mathrm{tr}(z(g) \rho_m(g))$.

A *Taylor-Wiles group* $T$ for $\Gamma$ has an open normal subgroup $H$ on which $\eta = 1$ and $\varepsilon \equiv 1 \bmod \ell$, elements $\sigma_1, \ldots, \sigma_q$ of $G_0$, and for each $N$ a frame $\Gamma_N \to \Gamma$ with $q$ new places of norm $\equiv 1 \bmod \ell^N$. Each new place has a Frobenius element near $\sigma_j$ and a tame generator. Let $H_\ell$ be the smallest closed normal subgroup of $\Gamma$ such that $H/H_\ell$ is a pro-$\ell$ group.

**Definition 5.6.3.** The point $\rho$ has *Selmer bound* $D$ for $T$ if there is $C$ such that for each $m$ and all large $N$, the set of traces of $\mathrm{Sel}_m$ for $\Gamma_N$ is finite with at most $|k|^{mD + C}$ elements.

The theorem below takes these conditions on $\rho$:

1. $\rho = 1$ on $G_0 \cap H_\ell$;
2. for a subgroup $D_0$ (*no invariants*): if $\varepsilon(g)\rho(g) Z = Z \rho(g)$ for all $g \in D_0$, then $Z = 0$;
3. for each $j$, the characteristic polynomial of $\rho(\sigma_j)$ is $\prod_i (X - \alpha_{j,i})$ with distinct $\alpha_{j,i} \in \mathcal{O}$;
4. *determined by traces* at $S$: if $z$ is a continuous cocycle for $\varepsilon \otimes \mathrm{ad}$ with values in $M_n(\mathcal{O})$, $P z(cgc^{-1}) = z(g)^T P$ and $\mathrm{tr}(z(\sigma)\rho(\sigma)^k) = 0$ for $\sigma \in S$ and $k \in \mathbb{N}$, then $a z$ is the coboundary of some $Y$ with $PY = Y^T P$, for some $a \neq 0$.

A *counting system* of degree $d$ for $T$ and $D_0$ gives, for each $N$, local and global Euler characteristic counts for $\Gamma_N$, local degrees $d_v$ with $\sum_v d_v = d$, and places whose decomposition groups are $D_0$ and contain the Frobenius and tame elements of $T$. We do not unfold it.

**Theorem 5.6.4 (Selmer trace bound).** Let $T$ be a Taylor-Wiles group, $\rho$ a point of dimension $n$ over $\mathcal{O}$ and $\alpha$ a matrix of eigenvalues. Let a counting system of degree $d$ for $T$ and $D_0$ be given. Assume $\ell \neq 2$; each open subgroup of $\Gamma$ has finitely many continuous homomorphisms to $\mathbb{Z}/\ell$; for each $v$ there is $g \in G_v$ with $\varepsilon(g) \neq 1$ in $\mathcal{O}$; and conditions 1 to 3 hold, with condition 4 at $S = \{\sigma_1, \ldots, \sigma_q\}$. Then $\rho$ has Selmer bound $nd + nq$ for $T$.

Lean: `UpperTheory.V.Th.b1absO`

*Proof.* The Greenberg-Wiles formula compares the Selmer group of $\mathrm{ad}_m$ with the dual Selmer group of $\varepsilon \otimes \mathrm{ad}_m$. We bound each term by a power of $|k|^m$ times a constant.

1. The local count at each $v$, with $\varepsilon \neq 1$ on $G_v$, gives a constant $C_v$ for the local condition at $v$.
2. Global invariants of $\mathrm{ad}_m$ have size at most $|k|^{c_1}$, because $\ell \neq 2$.
3. Invariants under $D_0$ have size at most $|k|^{c_0}$, by condition 2.
4. At the new place $j$, the Frobenius acts as $\sigma_j$ mod $\mathfrak{m}^m$ for large $N$. The invariants have size at most $|k|^{mn + C_j}$, by condition 3.
5. The dual Selmer group, cut by the new places, has size at most $|k|^{c_2}$ for large $N$. This uses $\varepsilon(c) = -1$, the finiteness of homomorphisms to $\mathbb{Z}/\ell$, condition 1 and condition 4.
6. The count at level $m$ gives the bound with exponent $m(nd + nq) + C$ plus a term that cancels. Take $C = c_0 + c_1 + c_2 + \sum_v C_v + \sum_j C_j$. $\square$

The next theorem applies this bound to the frames of a Hida setting. A *Hida setting* over a CM field $L$ has an odd prime $\ell$, an auxiliary place $v_0$, a set $S$ of places and, for each level $V$, a frame with Galois group of $L$ unramified outside $V$. Let $L^+$ be the maximal totally real subfield.

**Theorem 5.6.5 (Selmer bound for the ordinary Hecke algebra).** Assume the cohomology package (local and global Tate duality and the Euler characteristic formulas). Let $s$ be a Hida setting over $L$, $V_0$ a level with $S' = S$, $\mathcal{O}$ the ring of a coefficient datum, $r$ a residual datum of dimension $n$, $T$ a Taylor-Wiles group with Taylor-Wiles places, $\rho$ a point over $\mathcal{O}$ and $\alpha$ a matrix of eigenvalues. Assume local class field theory for $s$, $n \geq 1$, condition 1, condition 2 for the auxiliary decomposition group, condition 3, and condition 4 at $S = \{\sigma_j\}$ over $\overline{\mathbb{Q}}_\ell$. Then $\rho$ has Selmer bound $n[L^+ : \mathbb{Q}] + nq$ for $T$.

Lean: `UpperTheory.V.Th.b1O`

*Proof.* The ring $\mathcal{O}$ is a coefficient ring. Arithmetic presentations of the frames give a counting system of degree $[L^+ : \mathbb{Q}]$ for $T$ and the auxiliary group. The cohomology package and the oddness of $\ell$ give the counts. The frame satisfies the finiteness of homomorphisms to $\mathbb{Z}/\ell$. At each $v \mid \ell$ the cyclotomic character is not 1 on the decomposition group, and $\mathbb{Z}_\ell \to \mathcal{O}$ is injective, so $\varepsilon(g) \neq 1$ in $\mathcal{O}$. Condition 4 over $\overline{\mathbb{Q}}_\ell$ implies condition 4 over $\mathcal{O}$. Apply the Selmer trace bound. $\square$

### Ordinary cocycles are coboundaries

Let $s$ be a Hida setting, $V$ a level with $S' = S$, $r$ a residual datum and $B$ its universal ordinary determinant ring. A point $x$ of $B$ has characters $\psi_{v,i}$ at each $v \mid \ell$; it is *arithmetic* of weight $h$ if $h$ is increasing and each $\psi_{v,i}$ is locally algebraic of weight $h_{v,i}$.

**Theorem 5.6.6 (Hecke ideal for automorphic points).** Assume the hypothesis package H. Let $s$ be a Hida setting over $L$, $V$ a level with $S' = S$, $n \geq 1$, $r$ a residual datum, $B$ its universal ordinary determinant ring, $\Lambda$ a level datum and $\iota \colon \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$. Then there is an ideal $J$ of $B$ with these properties:

1. $J \subseteq \ker x$ for each arithmetic point $x$ of $B$ that comes from a continuous $\rho \colon G_L \to \mathrm{GL}_n(\overline{\mathbb{Q}}_\ell)$ with $2 \leq n \leq 4$, attached through $\iota$ to a cuspidal conjugate self-dual automorphic representation, trivial on the inertia at $v_0$, with a flag with characters $\psi_{v,i}$ at each $v \mid \ell$ and with $\psi_{v,i} \neq \psi_{v,j}\, \bar\varepsilon$ for all $i, j$;
2. there is a Taylor-Wiles base for $J$ of rank $n[L^+ : \mathbb{Q}]$ with the level condition, with weights in the inertia groups, and with the control condition at each arithmetic point.

Lean: `UpperTheory.V.Th.hidaX`

*Proof.* Take a Hida datum for the empty set of auxiliary places; its level is trivial. It gives an ideal $J$ cut out by the Hecke module. One lemma proves property 1 from this, and a second proves property 2. $\square$

**Definition 5.6.7.** Let $\rho \colon G_0 \to \mathrm{GL}_n(\overline{\mathbb{Q}}_\ell)$ be polarized by $P$ and let $x$ be a point of $B$. A function $z \colon G_0 \to M_n(\overline{\mathbb{Q}}_\ell)$ is an *ordinary cocycle* if it is continuous, $z(gg') = z(g) + \rho(g) z(g') \rho(g)^{-1}$, $P z(cgc^{-1}) = -z(g)^T P$, $z = 0$ on the inertia groups of $r$, and at each $v \mid \ell$ there are $w$ and $Y$ with $w^{-1}\rho w$ upper triangular on $G_v$ with diagonal $\psi_{v,i}$, $w^{-1}(z - dY) w$ upper triangular on $G_v$, and with zero diagonal on inertia. Here $dY(g) = \rho(g) Y \rho(g)^{-1} - Y$.

The pair $(\rho, P)$ is *regular* if there are $\sigma_1, \ldots, \sigma_q$ in the kernel of $\varepsilon$ with separable characteristic polynomials of $\rho(\sigma_j)$, and condition 4 holds at $\{\sigma_j\}$ over $\overline{\mathbb{Q}}_\ell$.

**Theorem 5.6.8 (ordinary cocycles at automorphic points).** Assume the hypothesis package H. Let $s$, $V$ with $S' = S$, a coefficient datum, $2 \leq n \leq 4$, $r$ with the conditions at $v_0$, $B$, $\iota$, a point $x$ arithmetic of weight $h$, $\rho$ and $P$ be given. Assume that the determinant of $x$ is the determinant of $\rho$, $\rho$ is continuous, its pull-back to $G_L$ is attached through $\iota$ to a cuspidal regular algebraic conjugate self-dual representation, $\rho(G_0)$ spans $M_n(\overline{\mathbb{Q}}_\ell)$, $\rho$ is polarized by $P$, $\rho = 1$ on the inertia at $v_0$, $\psi_{v,i} \neq \psi_{v,j}\, \bar\varepsilon$ on $G_v$ for all $v \mid \ell$ and all $i, j$, and $(\rho, P)$ is regular. Then each ordinary cocycle $z$ is a coboundary: $z = dY$ for some $Y$.

Lean: `UpperTheory.V.Th.ordVan2`

*Proof.* The proof has these steps.

1. Build the cohomology package from H. The character $\varepsilon$ of the frame is $\bar\varepsilon$ on each decomposition group.
2. An integral model gives a new coefficient ring, a residual datum $r'$, its ring $B'$, a point $x'$ of $B'$ and a derivation $\delta$ at $x'$ that kills the inertia characters. If $\delta$ kills all traces, then $z$ is a coboundary.
3. A level datum exists by local class field theory. The previous theorem gives an ideal $J$ of $B'$.
4. The flags of $z$ and the hypothesis on $\psi$ give the inputs of property 1 at $x'$. So $J \subseteq \ker x'$.
5. [The core argument](/entry/core-o-of-literal-automorphy-n/), with property 2, $J \subseteq \ker x'$ and regularity, shows that $\delta$ kills all traces. It uses the Selmer bound for the ordinary Hecke algebra. Step 2 ends the proof. $\square$

**Theorem 5.6.9 (core).** Assume the hypothesis package H and the cohomology package. Let $s$ be a Hida setting over $L$, $V$ a level with $S' = S$, and assume that $L$ has no primitive $\ell$-th root of unity. Let the coefficient datum contain the images of the integers of $L$, let $2 \leq n \leq 4$, and let $r$ satisfy the conditions at $v_0$. Let $x$ be a point of $B$ and $\rho$ a representation such that $(x, \rho)$ is a nice automorphic point: $\rho$ is continuous, $x$ is arithmetic and comes from $\rho$, $\rho$ is automorphic through $\iota$ and trivial on the inertia at $v_0$, it has a flag at each $v \mid \ell$, the characters at $v$ are free, $\rho$ is residually irreducible on the kernel of $\varepsilon$, and a third condition holds that we do not unfold. Then for each polarization $P$ of $\rho$ and each extension $R$ of the adjoint action to $\Gamma$, each cocycle of $R$ that is ordinary for the characters of $x$ is a coboundary of $R$.

Lean: `UpperTheory.V.Th.core`

*Proof.* Take the weight and determinant of $x$. Irreducibility gives that $\rho(G_0)$ spans $M_n$, and then $\rho = 1$ on the inertia groups of $r$. Normalize $z$ by a coboundary $dX_0$ so that it is polarized. The conditions at $v_0$ give $\varepsilon \neq 1$ on $G_0$. The finiteness of homomorphisms to $\mathbb{Z}/\ell$, from the cohomology package, and irreducibility give regularity. For $i = j$, $\psi_{v,i} \neq \psi_{v,i}\bar\varepsilon$ because $\bar\varepsilon \neq 1$ on $G_v$. For $i \neq j$, freeness gives $g$ with $\varepsilon(g) = 1$ and $\psi_{v,i}(g) \neq \psi_{v,j}(g)$. The previous theorem, applied to $z - dX_0$, gives the coboundary. $\square$

**Remark 5.6.10 (Formalization).** The Selmer trace bound is in [ResidualRepOne.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/CyclicReductionCohomology/ResidualRepOne.lean#L44). The file is named after the private helper `residual_rep_one` at line 35. Steps 1 to 6 are `locVO`, `h0GO`, `h0v0O`, `h0qO`, `dualNO` and `oneLevelO`, which we do not unfold. The statement has no hypothesis $1 \leq n$. The counting system is `Sys` and condition 4 is `DetO` ([DualPair.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/CyclicReductionCohomology/DualPair.lean#L51)). The Selmer bound is `B1` and the point is `Pt` ([OrdinaryHeckeAlgebraIntegral.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/OrdinaryHeckeAlgebraIntegral.lean#L64)). The second theorem proves `ordinaryHeckeAlgebraIntegral` (line 208 there), but it lives in another file of the same name, [GaloisRepresentationTypes/OrdinaryHeckeAlgebraIntegral.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/GaloisRepresentationTypes/OrdinaryHeckeAlgebraIntegral.lean#L31). Its intro pattern at line 32 drops the hypotheses `LocCFT s` and `1 ≤ n`, so these are unused. The name `b1O` says little. The Hecke ideal theorem is in [HidaX.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/GaloisRepresentationTypes/HidaX.lean#L8); its steps are `hdEx`, `jEx`, `jPT` and `levelX`. The predicate `IsJ` allows $J = B$ when the Hecke module is zero; then property 1 says that no such point exists. We have not unfolded `TWBase`, `LevAt` or `CtrlH`. The theorem on ordinary cocycles is at [OrdVan.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/GaloisRepresentationTypes/OrdVan.lean#L183), and its statement `OrdVan2` is at [OrdVan2.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/OrdVan2.lean#L10). Step 2 is the private lemma `nmAbs`, and step 5 is `coreO`. The hypothesis on $\psi$ is for all $i, j$, also $i = j$; the sibling `OrdVan` at line 230 of OrdinaryHeckeAlgebraIntegral.lean asks only $i < j$. The core is at [VwinOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/VwinOf.lean#L10), as `core_of (ordVan2 hH) (W.phiAll hC)` with `core_of` at [CoreOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/GaloisRepresentationTypes/CoreOf.lean#L24). The statement `Core` is at [OrdZero.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/OrdZero.lean#L76), and a nice automorphic point is `NiceAPt`; its third condition is `N3`. The core takes the cohomology package `CohP` as a hypothesis, but `ordVan2` builds its own `CohP` from H at line 188 of OrdVan.lean, so the hypothesis is needed only for `phiAll`.
