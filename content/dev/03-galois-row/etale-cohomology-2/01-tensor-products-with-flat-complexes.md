---
title: Tensor products with flat complexes
decls:
  - LateralTheory.Fin.EtaleTensorPairQuasiIsoOfFlatQuasiIso.intersectionNumber_baseChange
  - LateralTheory.Fin.EtaleTensorPairQuasiIsoOfFlatQuasiIso.etale_tensor_quasiIso_of_acyclic_cone
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Tensor products with flat complexes

Let $f : I \to I'$ be a quasi-isomorphism of complexes of sheaves, and let $J$ be a complex of flat sheaves. If all complexes are bounded below, then $f \otimes 1 : I \otimes J \to I' \otimes J$ is again a quasi-isomorphism. This section proves this fact for sheaves on the big étale site, in [Theorem 4.1.7](/entry/etale-tensor-quasi-iso-of-acyclic-cone/). The cup product on [[étale cohomology|7YX76G0838]] is made from pairings of complexes, and the theorem shows that the product does not depend on the choice of the complexes. It is an input to [the ring laws of the cup product](/entry/s41/).

We fix a commutative ring $R$. A *sheaf* in this section is a sheaf of $R$-modules on the category of schemes with the [[Grothendieck topology|GDRFSJ8E2B]] of étale coverings. For a sheaf $F$ and a scheme $U$ we write $F(U)$ for the module of sections, and $s \mapsto s|_V$ for the restriction along a map $g : V \to U$. A *complex* is a cochain complex of sheaves indexed by $\mathbb{Z}$. A complex $C$ is *bounded below by* $a$ if $C^n = 0$ for all $n < a$. For the [[tensor product|F0HQXQ0HCD]] of modules see [the Background](/learn/algebra/#tensor-products-and-coinvariants).

**Definition 4.1.1 (Local property).** Let $U$ be a scheme and let $P$ be a property of maps $g : V \to U$. We say that $P$ holds *locally on* $U$ if there is an étale covering sieve $S$ of $U$ such that $P(g)$ holds for each $g$ in $S$.

**Definition 4.1.2 (Locally exact complex).** A complex $C$ is *acyclic* if all its cohomology sheaves are zero. It is *locally exact* if for each scheme $U$, each $n$ and each $z \in C^n(U)$ with $dz = 0$, locally on $U$ there is $y \in C^{n-1}(V)$ with $dy = z|_V$.

**Definition 4.1.3 (Pairing).** Let $I$, $J$ and $K$ be complexes. A *pairing* $\mu : (I, J) \to K$ is a family of $R$-bilinear maps $I^s(U) \times J^t(U) \to K^{s+t}(U)$, $(a, b) \mapsto ab$, one for each scheme $U$ and all $s, t$, with two properties. First, $(ab)|_V = a|_V\, b|_V$ for each $g : V \to U$. Second, the Leibniz rule holds:
$$d(ab) = (da)\, b + (-1)^s\, a\, (db).$$

A pairing gives an $R$-linear map
$$\lambda_U : \mathrm{Tens}^w(U) = \bigoplus_{s + t = w} I^s(U) \otimes_R J^t(U) \longrightarrow K^w(U).$$
We write $D$ for the total differential of $\mathrm{Tens}^\bullet(U)$, so that $\lambda_U(Dx) = d\lambda_U(x)$ by the Leibniz rule.

**Definition 4.1.4 (Tensor pairing).** A pairing $\mu$ is a *tensor pairing* if each $\lambda_U$ is locally surjective and has a locally zero kernel. That is: each $y \in K^w(U)$ is locally of the form $\lambda_V(x)$, and each $x$ with $\lambda_U(x) = 0$ satisfies $x|_V = 0$ locally on $U$.

So $K^w$ is the sheaf associated to the presheaf $U \mapsto \mathrm{Tens}^w(U)$, and $K$ is a model of the tensor product complex $I \otimes J$. We do not fix one model. All statements below hold for each tensor pairing.

**Definition 4.1.5 (Compatible maps).** Let $\tau : (I, J) \to T$ and $\tau' : (I', J) \to T'$ be pairings, and let $f : I \to I'$ and $u : T \to T'$ be maps of complexes. The pair $(f, u)$ is *compatible* if $u(ab) = f(a)\, b$ for all sections $a$ of $I$ and $b$ of $J$.

**Definition 4.1.6 (Flat sheaf).** A sheaf $M$ is *flat* if there are a presheaf $P$ of $R$-modules and a map $\varphi : P \to M$ such that $\varphi$ is locally surjective, the kernel of $\varphi$ is locally zero, and $P(U)$ is a [[flat module|73RYYEVDKA]] over $R$ for each nonempty scheme $U$.

A sheaf $M$ such that $M(U)$ is flat for each $U$ is flat in this sense, with $P = M$ and $\varphi$ the identity. The main result of the section is the following.

**Theorem 4.1.7 (Tensor product with a flat complex).** Let $I$, $I'$ and $J$ be complexes that are bounded below by $0$, with $J^t$ flat for each $t$. Let $\tau : (I, J) \to T$ and $\tau' : (I', J) \to T'$ be tensor pairings. Let $f : I \to I'$ be a quasi-isomorphism and $u : T \to T'$ a map such that $(f, u)$ is compatible. Then $u$ is a quasi-isomorphism.

Lean: `LateralTheory.Fin.EtaleTensorPairQuasiIsoOfFlatQuasiIso.etale_tensor_quasiIso_of_acyclic_cone` (also `LateralTheory.Fin.EtaleTensorPairQuasiIsoOfFlatQuasiIso.intersectionNumber_baseChange`, a second name).

The proof reduces the theorem to the case of an acyclic complex, with the mapping cone. We need four lemmas.

**Lemma 4.1.8 (Cone criterion).** A map $f$ of complexes is a quasi-isomorphism if and only if its mapping cone is acyclic. If $I$ and $I'$ are bounded below by $0$, then the cone of any map $f : I \to I'$ is bounded below by $-1$.

Lean: `qis_iff_cone` (also `cone_ge`).

*Proof.* The first claim is C. A. Weibel, *An Introduction to Homological Algebra*, Corollary 1.5.4, in the abelian category of sheaves. It follows from the long exact sequence of cohomology of the triangle $I \to I' \to \mathrm{cone}(f) \to I[1]$. The cone in degree $n$ is $I^{n+1} \oplus I'^n$, which gives the bound. $\square$

**Lemma 4.1.9 (Cones of pairings).** Let $\tau : (I, J) \to T$ and $\tau' : (I', J) \to T'$ be tensor pairings, and let $f : I \to I'$ and $u : T \to T'$ be maps such that $(f, u)$ is compatible. Then there is a tensor pairing $\sigma : (\mathrm{cone}(f), J) \to \mathrm{cone}(u)$.

Lean: `LateralTheory.EtaleFoundations.tqis.cone_of`.

*Proof.* A section of $\mathrm{cone}(f)^s$ is a pair $(a, a')$ with $a \in I^{s+1}$ and $a' \in I'^s$. Put $\sigma((a, a'), b) = (\tau(a, b), \tau'(a', b))$ in $\mathrm{cone}(u)^{s+t} = T^{s+t+1} \oplus T'^{s+t}$. The Leibniz rule for $\sigma$ follows from the Leibniz rules of $\tau$ and $\tau'$ and from compatibility, which gives $u(\tau(a, b)) = \tau'(f(a), b)$. The map $\lambda$ of $\sigma$ is the direct sum of the maps $\lambda$ of $\tau$ and $\tau'$, after a shift of the index. So it is locally surjective with a locally zero kernel. $\square$

**Lemma 4.1.10 (Columns).** Let $C$ be a locally exact complex and let $J$ be a complex with $J^t$ flat for each $t$. Then for each $t$ the column $C \otimes J^t$ is locally exact on sections. That is: if $x \in C^s(U) \otimes_R J^t(U)$ and $(d \otimes 1)(x) = 0$, then locally on $U$ there is $y \in C^{s-1}(V) \otimes_R J^t(V)$ with $(d \otimes 1)(y) = x|_V$.

Lean: `LateralTheory.EtaleFoundations.acyc.column_of`.

*Proof.* Let $\varphi : P \to J^t$ be as in the definition of a flat sheaf. There are three steps.

First, we lift $x$. Write $x = \sum_j c_j \otimes b_j$, a finite sum. Since $\varphi$ is locally surjective, locally each $b_j$ is $\varphi(p_j)$. So locally $x$ is the image of $\tilde{x} = \sum_j c_j \otimes p_j$ in $C^s(V) \otimes P(V)$.

Second, we show: for each sheaf $G$ and each scheme $V$, the kernel of $G(V) \otimes P(V) \to G(V) \otimes J^t(V)$ is locally zero. Let $w = \sum_j g_j \otimes p_j$ map to $0$. Then $\sum_j g_j \otimes \varphi(p_j) = 0$ already in $G(V) \otimes Q$ for a finitely generated submodule $Q \subseteq J^t(V)$ that contains the $\varphi(p_j)$. A tensor that is zero in $G(V) \otimes Q$ vanishes for a finite set of linear relations: there are finitely many $y_\kappa \in G(V)$ and coefficients with $g_j = \sum_\kappa a_{j\kappa} y_\kappa$, and with $\sum_j a_{j\kappa} \varphi(p_j)$ equal to a combination of generators of $Q$ that is killed by the same relations. Each of these finitely many relations in $J^t(V)$ lifts to $P$ locally, because $\varphi$ is locally surjective with a locally zero kernel. After these refinements $w$ is zero. This step does not use flatness.

Third, we use flatness. By the second step, $(d \otimes 1)(\tilde{x})$ is locally zero. If $V$ is empty, all modules of sections are zero and there is nothing to prove. Otherwise $P(V)$ is flat, so tensoring with $P(V)$ keeps kernels: $\ker(d \otimes 1) = \ker(d) \otimes P(V)$. So $\tilde{x} = \sum_i z_i \otimes p_i$ with $dz_i = 0$. Since $C$ is locally exact, locally $z_i = dy_i$. Then $y = \sum_i y_i \otimes \varphi(p_i)$ satisfies $(d \otimes 1)(y) = x$ locally. $\square$

**Lemma 4.1.11 (Staircase).** Let $C$ be bounded below by $a$ and $J$ bounded below by $b$. Let $\tau : (C, J) \to T$ be a tensor pairing such that each column $C \otimes J^t$ is locally exact on sections, in the sense of the column lemma. Then $T$ is locally exact.

Lean: `LateralTheory.EtaleFoundations.acyc.stair_of` (also `LateralTheory.EtaleFoundations.StepPf.Step_of`, the step of the induction).

*Proof.* Let $z \in T^n(U)$ with $dz = 0$. Locally, $z = \lambda(x)$ with $x \in \mathrm{Tens}^n$, and $x$ has components $x_{s,t} \in C^s \otimes J^t$ with $s + t = n$.

The step. Assume that $x_{s,t} = 0$ for $t < t_0$. Since $\lambda(Dx) = dz = 0$ and the kernel of $\lambda$ is locally zero, $Dx$ is locally zero. Its component in $C^{n+1-t_0} \otimes J^{t_0}$ is $(d \otimes 1)(x_{n-t_0, t_0})$, because the other term comes from $x_{n+1-t_0, t_0-1} = 0$. So $(d \otimes 1)(x_{n-t_0, t_0})$ is locally zero. By the hypothesis on the columns, locally $x_{n-t_0, t_0} = (d \otimes 1)(y)$ for some $y \in C^{n-1-t_0} \otimes J^{t_0}$. Then $x' = x - Dy$ has $x'_{s,t} = 0$ for $t < t_0 + 1$, and locally $x = x' + Dy$.

The induction. If $t > n - a$, then $s = n - t < a$ and $C^s = 0$, so $x_{s,t} = 0$. If $t < b$, then $J^t = 0$. Start with $t_0 = b$ and apply the step $n - a - b + 1$ times. Each application replaces $x$ by $x' + Dy$ locally, and $\lambda(x') = z - d\lambda(y)$ again has $d\lambda(x') = 0$. At the end $x' = 0$, so locally $x = DY$ and $z = d\lambda(Y)$. $\square$

**Proposition 4.1.12 (Tensor of an acyclic complex).** Let $C$ be bounded below by $a$ and acyclic, let $J$ be bounded below by $b$ with $J^t$ flat for each $t$, and let $\tau : (C, J) \to T$ be a tensor pairing. Then $T$ is acyclic.

Lean: `LateralTheory.EtaleFoundations.tqis.acyc_of` (also `LateralTheory.EtaleFoundations.acyc.acycIff_of`, the equivalence of acyclic and locally exact).

*Proof.* A complex of sheaves is acyclic if and only if it is locally exact. The reason is that a section of a cohomology sheaf is zero exactly when it is locally zero. So $C$ is locally exact. By the column lemma each column $C \otimes J^t$ is locally exact on sections. By the staircase lemma, $T$ is locally exact, so $T$ is acyclic. $\square$

*Proof of the theorem.* By the cone criterion, $\mathrm{cone}(f)$ is acyclic and bounded below by $-1$. By the lemma on cones of pairings there is a tensor pairing $\sigma : (\mathrm{cone}(f), J) \to \mathrm{cone}(u)$. The proposition on acyclic complexes with $a = -1$ and $b = 0$ shows that $\mathrm{cone}(u)$ is acyclic. By the cone criterion again, $u$ is a quasi-isomorphism. $\square$

The étale topology plays no special role in the argument. We only use that a section of a sheaf is zero if it is locally zero, and that a covering sieve can be refined.

**Remark 4.1.13 (Formalization).** The flatness of the definition of a flat sheaf is weak: it asks for a flat presheaf $P$ only on nonempty schemes, and only up to local isomorphism with $J^t$. The results on the cup product apply the theorem to sheaves whose modules of sections are all flat; see [LeafTensQIsoGenPf.lean](lean:Development/EtaleCohomology/EtaleSheaves/LeafTensQIsoGenPf.lean#L12). The two Lean names of the theorem do not describe it: the second speaks of an intersection number and a base change, and the theorem has neither. The Lean proof applies the reduction to the acyclic case and the lemma on cones of pairings; see [EtaleComplexAcyclicIffLocalExactness.lean](lean:Development/EtaleCohomology/TateTwists/EtaleComplexAcyclicIffLocalExactness.lean#L22).
