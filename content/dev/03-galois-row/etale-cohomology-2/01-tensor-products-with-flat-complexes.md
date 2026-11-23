---
title: Tensor products with flat complexes
decls:
  - LateralTheory.Fin.EtaleTensorPairQuasiIsoOfFlatQuasiIso.intersectionNumber_baseChange
  - LateralTheory.Fin.EtaleTensorPairQuasiIsoOfFlatQuasiIso.etale_tensor_quasiIso_of_acyclic_cone
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Tensor products with flat complexes

Let $f : I \to I'$ be a quasi-isomorphism of complexes of sheaves, and let $J$ be a complex of flat sheaves. If all complexes are bounded below, then $f \otimes 1 : I \otimes J \to I' \otimes J$ is again a quasi-isomorphism. This section proves this fact for sheaves on the big étale site. The cup product on [[étale cohomology|7YX76G0838]] is made from pairings of complexes, and the fact shows that the product does not depend on the choice of the complexes. It is an input to [the ring laws of the cup product](/entry/s41/).

We fix a commutative ring $R$. A *sheaf* in this section is a sheaf of $R$-modules on the category of schemes with the [[Grothendieck topology|GDRFSJ8E2B]] of étale coverings. For a sheaf $F$ and a scheme $U$ we write $F(U)$ for the module of sections, and $s \mapsto s|_V$ for the restriction along a map $g : V \to U$. A *complex* is a cochain complex of sheaves indexed by $\mathbb{Z}$. A complex $C$ is *bounded below by* $a$ if $C^n = 0$ for all $n < a$. For the [[tensor product|F0HQXQ0HCD]] of modules see [the Background](/learn/algebra/#tensor-products-and-coinvariants).

**Definition (Local property).** Let $U$ be a scheme and let $P$ be a property of maps $g : V \to U$. We say that $P$ holds *locally on* $U$ if there is an étale covering sieve $S$ of $U$ such that $P(g)$ holds for each $g$ in $S$.

**Definition (Locally exact complex).** A complex $C$ is *acyclic* if all its cohomology sheaves are zero. It is *locally exact* if for each scheme $U$, each $n$ and each $z \in C^n(U)$ with $dz = 0$, locally on $U$ there is $y \in C^{n-1}(V)$ with $dy = z|_V$.

**Definition (Pairing).** Let $I$, $J$ and $K$ be complexes. A *pairing* $\mu : (I, J) \to K$ is a family of $R$-bilinear maps $I^s(U) \times J^t(U) \to K^{s+t}(U)$, $(a, b) \mapsto ab$, one for each scheme $U$ and all $s, t$, with two properties. First, $(ab)|_V = a|_V\, b|_V$ for each $g : V \to U$. Second, the Leibniz rule holds:
$$d(ab) = (da)\, b + (-1)^s\, a\, (db).$$

A pairing gives an $R$-linear map
$$\lambda_U : \mathrm{Tens}^w(U) = \bigoplus_{s + t = w} I^s(U) \otimes_R J^t(U) \longrightarrow K^w(U).$$

**Definition (Tensor pairing).** A pairing $\mu$ is a *tensor pairing* if each $\lambda_U$ is locally surjective and has a locally zero kernel. That is: each $y \in K^w(U)$ is locally of the form $\lambda_V(x)$, and each $x$ with $\lambda_U(x) = 0$ satisfies $x|_V = 0$ locally on $U$.

So $K^w$ is the sheaf associated to the presheaf $U \mapsto \mathrm{Tens}^w(U)$, and $K$ is a model of the tensor product complex $I \otimes J$. The code does not choose one model. It works with any tensor pairing.

**Definition (Compatible maps).** Let $\tau : (I, J) \to T$ and $\tau' : (I', J) \to T'$ be pairings, and let $f : I \to I'$ and $u : T \to T'$ be maps of complexes. The pair $(f, u)$ is *compatible* if $u(ab) = f(a)\, b$ for all sections $a$ of $I$ and $b$ of $J$.

**Definition (Flat sheaf).** A sheaf $M$ is *flat* if there are a presheaf $P$ of $R$-modules and a map $\varphi : P \to M$ such that $\varphi$ is locally surjective, the kernel of $\varphi$ is locally zero, and $P(U)$ is a [[flat module|73RYYEVDKA]] over $R$ for each nonempty scheme $U$.

The main result of the section is the following.

**Theorem (Tensor product with a flat complex).** Let $I$, $I'$ and $J$ be complexes that are bounded below by $0$, with $J^t$ flat for each $t$. Let $\tau : (I, J) \to T$ and $\tau' : (I', J) \to T'$ be tensor pairings. Let $f : I \to I'$ be a quasi-isomorphism and $u : T \to T'$ a map such that $(f, u)$ is compatible. Then $u$ is a quasi-isomorphism.

Lean: `LateralTheory.Fin.EtaleTensorPairQuasiIsoOfFlatQuasiIso.etale_tensor_quasiIso_of_acyclic_cone` (also `LateralTheory.Fin.EtaleTensorPairQuasiIsoOfFlatQuasiIso.intersectionNumber_baseChange`, a second name).

The proof reduces the theorem to the case of an acyclic complex, with the mapping cone. We need four lemmas.

**Lemma (Cone criterion).** A map $f$ of complexes is a quasi-isomorphism if and only if its mapping cone is acyclic. If $I$ and $I'$ are bounded below by $0$, then the cone of $f$ is bounded below by $-1$.

Lean: `qis_iff_cone` (also `cone_ge`).

*Proof.* The first claim is C. A. Weibel, *An Introduction to Homological Algebra*, Corollary 1.5.4, in the abelian category of sheaves. The code takes it from the long exact sequence of the cone triangle in the homotopy category. The cone in degree $n$ is $I^{n+1} \oplus I'^n$, which gives the bound. $\square$

**Lemma (Cones of pairings).** Let $\tau$, $\tau'$, $f$ and $u$ be as in the theorem, without the conditions on bounds and flatness. Then there is a tensor pairing $\sigma : (\mathrm{cone}(f), J) \to \mathrm{cone}(u)$.

Lean: `LateralTheory.EtaleFoundations.tqis.cone_of`.

*Proof.* A section of $\mathrm{cone}(f)^s$ is a pair $(a, a')$ with $a \in I^{s+1}$ and $a' \in I'^s$. Put $\sigma((a, a'), b) = (\tau(a, b), \tau'(a', b))$ in $\mathrm{cone}(u)^{s+t} = T^{s+t+1} \oplus T'^{s+t}$. The Leibniz rule for $\sigma$ follows from the Leibniz rules of $\tau$ and $\tau'$ and from compatibility, which gives $u(\tau(a, b)) = \tau'(f(a), b)$. The map $\lambda$ of $\sigma$ is the direct sum of the maps $\lambda$ of $\tau$ and $\tau'$, after a shift of the index. So it is locally surjective with a locally zero kernel. $\square$

**Lemma (Columns).** Let $C$ be a locally exact complex and let $J$ be a complex of flat sheaves. Then for each $t$ the column $C \otimes J^t$ is locally exact on sections. That is: if $x \in C^s(U) \otimes_R J^t(U)$ and $(d \otimes 1)(x) = 0$, then locally on $U$ there is $y \in C^{s-1}(V) \otimes_R J^t(V)$ with $(d \otimes 1)(y) = x|_V$.

Lean: `LateralTheory.EtaleFoundations.acyc.column_of`.

*Proof.* Let $\varphi : P \to J^t$ be as in the definition of a flat sheaf. There are two steps. First, we lift $x$ to $C^s(V) \otimes P(V)$, locally on $U$. Here we need that the kernel of $G(V) \otimes P(V) \to G(V) \otimes J^t(V)$ is locally zero for each sheaf $G$. A tensor in this kernel is a finite sum. By the equational criterion (H. Matsumura, *Commutative Ring Theory*, Theorem 7.6, in the form for a finite relation), each relation that makes it zero in $G(V) \otimes J^t(V)$ comes from finitely many relations in $J^t(V)$. Each of them holds in $P$ after a refinement, since $\varphi$ has a locally zero kernel. This step needs no flatness. Second, we use that $P(V)$ is flat. Then $C^{s-1}(V) \otimes P(V) \to C^s(V) \otimes P(V) \to C^{s+1}(V) \otimes P(V)$ is exact where $C$ is exact, and $C$ is exact on sections after refinement. Again we pass to a covering for each element. When $V$ is empty, all modules are zero and there is nothing to prove. $\square$

**Lemma (Staircase).** Let $C$ be bounded below by $a$ and $J$ bounded below by $b$. Let $\tau : (C, J) \to T$ be a tensor pairing such that each column $C \otimes J^t$ is locally exact in the sense of the previous lemma. Then $T$ is locally exact.

Lean: `LateralTheory.EtaleFoundations.acyc.stair_of` (also `LateralTheory.EtaleFoundations.StepPf.Step_of`, the step of the induction).

*Proof.* Let $z \in T^n(U)$ with $dz = 0$. Locally, $z = \lambda(x)$ with $x \in \mathrm{Tens}^n$, and $x$ has components $x_{s,t} \in C^s \otimes J^t$ with $s + t = n$. Let $t_0$ be the least $t$ with $x_{s,t} \ne 0$. The component of $\lambda(dx)$ of lowest $J$-degree is $(d \otimes 1)(x_{n-t_0, t_0})$, and it is locally zero because $dz = 0$ and the kernel of $\lambda$ is locally zero. By the column lemma, locally $x_{n - t_0, t_0} = (d \otimes 1)(y)$. Then $x - Dy$ has no component with $t \le t_0$, where $D$ is the total differential of $\mathrm{Tens}$. This is the step of the induction: locally $x = x' + Dy$ with $x'$ zero in $J$-degree up to $t_0$. The bounds stop the induction: since $C^s = 0$ for $s < a$, all components with $t > n - a$ are zero, and $t$ starts at $b$. After $n - a - b + 1$ steps we have $x = DY$ locally, so $z = d\lambda(Y)$ locally. $\square$

**Proposition (Tensor of an acyclic complex).** Let $C$ be bounded below by $a$ and acyclic, let $J$ be bounded below by $b$ with $J^t$ flat for each $t$, and let $\tau : (C, J) \to T$ be a tensor pairing. Then $T$ is acyclic.

Lean: `LateralTheory.EtaleFoundations.tqis.acyc_of` (also `LateralTheory.EtaleFoundations.acyc.acycIff_of`, the equivalence of acyclic and locally exact).

*Proof.* A complex of sheaves is acyclic if and only if it is locally exact. The reason is that a section of a cohomology sheaf is zero exactly when it is locally zero. So $C$ is locally exact. By the column lemma each column $C \otimes J^t$ is locally exact. By the staircase lemma $T$ is locally exact, so $T$ is acyclic. $\square$

*Proof of the theorem.* By the cone criterion, $\mathrm{cone}(f)$ is acyclic and bounded below by $-1$. By the lemma on cones there is a tensor pairing $\sigma : (\mathrm{cone}(f), J) \to \mathrm{cone}(u)$. The proposition with $a = -1$ and $b = 0$ shows that $\mathrm{cone}(u)$ is acyclic. By the cone criterion again, $u$ is a quasi-isomorphism. $\square$

**Remark.** The étale topology plays no special role in the argument. Only the facts that sheaf cohomology is detected locally and that a covering sieve can be refined are used. The flatness in the code is weak: it asks for a flat presheaf $P$ only on nonempty schemes, and only up to local isomorphism with $J^t$. A sheaf whose modules of sections are all flat is flat in this sense, with $P = M$ and $\varphi$ the identity. This is the form in which the code on the cup product applies the theorem; see [LeafTensQIsoGenPf.lean](lean:Development/EtaleCohomology/EtaleSheaves/LeafTensQIsoGenPf.lean#L12).

**Remark.** The two Lean names of the theorem do not describe it. The second name speaks of an intersection number and a base change, and the theorem has neither. The Lean folder puts the result in a module on Tate twists, under the name of local exactness. The code states the theorem as one proposition, and the proof is a single application of the reduction to the acyclic case and the lemma on cones; see [EtaleComplexAcyclicIffLocalExactness.lean](lean:Development/EtaleCohomology/TateTwists/EtaleComplexAcyclicIffLocalExactness.lean#L22).
