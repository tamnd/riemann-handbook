---
title: Theta level objects and the Kodaira-Spencer map
decls:
  - GlobalTheory.KS.KerZero.derivation_eq_zero_of_ks_zero
  - GlobalTheory.T.derivation_eq_zero_of_kodairaSpencer_zero
  - GlobalTheory.KS.tangent_injects_symm_antilinear
  - GlobalTheory.T.tangent_injects_symmetric_antilinear_commuting
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta level objects and the Kodaira-Spencer map

The moduli spaces of this chapter are built as families of *theta level objects*: principally polarized abelian schemes with a full level structure, a Weil pairing in standard form and an action of a set of endomorphisms. This section defines them and proves the first-order statement on which the dimension count of the next section rests. Let $R$ be the coordinate ring of a family of theta level objects and fix a complex point of it. To each tangent vector of $\operatorname{Spec} R$ at that point we attach a complex $g \times g$ matrix, its Kodaira-Spencer class, read off from the complex uniformization of the fibre. We prove that this map is injective, that its values are symmetric for the hermitian form of the polarization, and that they commute antilinearly with every endomorphism of the family. The background is [the complex uniformization](/learn/abelian-varieties/#the-complex-uniformization) and [the Kodaira-Spencer map](/learn/abelian-varieties/#the-kodaira-spencer-map). The result is used in [the tangent bound for PEL families](/entry/finrank-derivation-le/).

Throughout, we assume the laws of abelian schemes (the twenty-four facts about abelian schemes and their line bundles fixed in the chapter on polarizations and theta characteristics) and four further facts of the same kind: base change for sections over any base, twisting of sections, the pairing of characters and the density of smooth points. We call the second list *the second laws*. We also assume *the uniformization theorem*: every principally polarized abelian variety $(A, L)$ over $\mathbb{C}$ with a rigidification has a uniformization $\mathbb{C}^g \to A(\mathbb{C})$ under which $L$ is the line bundle of Appell-Humbert data, sections of $L^n$ are theta functions for those data, tangent vectors are constant vector fields, and endomorphisms lift to linear maps (D. Mumford, *Abelian Varieties*, §1 to §3).

**Definition 5.1.1 (Base of level k).** Let $o$ be a commutative ring and $k \ge 1$. A *base of level* $k$ on $o$ is a unit $\zeta \in o^\times$ such that $k$ is a unit in $o$ and, for every ring map $\beta : o \to K$ to a field, $\beta(\zeta)$ is a primitive $k$-th root of unity in $K$.

Lean: `GlobalTheory.ZM.TBase`.

For example $o = \mathbb{Z}[\zeta_k, 1/k]$ with $\zeta = \zeta_k$ is a base of level $k$, and so is $\mathbb{C}$ with $\zeta = e^{2\pi i/k}$.

Let $\omega$ be the standard symplectic form on $\mathbb{Z}^{2g}$: $\omega(e_i, e_j) = 1$ if $i < g$ and $j = i + g$, $\omega(e_i, e_j) = -1$ if $j < g$ and $i = j + g$, and $\omega(e_i, e_j) = 0$ otherwise.

**Definition 5.1.2 (Theta level object).** Let $o$ carry a base $\zeta$ of level $k$, let $J$ be a set and let $s : S \to \operatorname{Spec} o$ be a scheme over $o$. A *theta level object* of genus $g$ and level $k$ over $S$, with endomorphisms indexed by $J$, consists of:

1. an abelian scheme $A \to S$ (see [[abelian schemes|JDDXZ89N33]]), [[smooth|EXKGG9X6J0]] of relative dimension $g$;
2. a line bundle $L$ on $A$, rigidified along the zero section, symmetric and relatively ample, whose group $K(L)$ is trivial, so that $L$ is a principal polarization;
3. sections $P_1, \dots, P_{2g} \in A(S)$ with $k P_i = 0$, such that at every geometric point of $S$ each point $y$ with $k y = 0$ is $\sum_i c_i P_i$ for a unique $c \in (\mathbb{Z}/k)^{2g}$;
4. the Weil pairing of level $k$ attached to $L$ satisfies $e_k(P_i, P_j) = \zeta^{\omega(e_i, e_j)}$;
5. for each $j \in J$ an endomorphism $\alpha_j$ of the group scheme $A$.

For $a \in (\mathbb{Z}/k)^{2g}$ we write $P_a = \sum_i a_i P_i$ for the *labelled point* $a$.

Lean: `GlobalTheory.ZM.TObj`, `GlobalTheory.ZM.TObj.pol`, `GlobalTheory.ZM.TObj.lab`.

So a theta level object is a principally polarized abelian scheme with a symplectic level-$k$ structure in the sense of [Siegel moduli schemes and level structures](/learn/abelian-varieties/#siegel-moduli-schemes-and-level-structures), with a family of endomorphisms added.

**Definition 5.1.3 (Map of theta level objects).** Let $t'$ and $t$ be theta level objects over $S'$ and $S$ and let $f : S' \to S$ be a map over $o$. A *map* $t' \to t$ over $f$ is a morphism $\varphi : A' \to A$ that identifies $A'$ with the pullback $f^* A$ as group schemes, with $L' \cong \varphi^* L$, $\varphi \circ P'_i = P_i \circ f$ for all $i$ and $\varphi \circ \alpha'_j = \alpha_j \circ \varphi$ for all $j$.

Lean: `GlobalTheory.ZM.TMap`.

Let $k$ be a field and $k[\varepsilon]$ the ring of dual numbers. For a point $x : \operatorname{Spec} k[\varepsilon] \to X$, the *constant point* $\bar x$ is the composite $\operatorname{Spec} k[\varepsilon] \to \operatorname{Spec} k \to \operatorname{Spec} k[\varepsilon] \xrightarrow{x} X$. It is the tangent vector zero at the closed point of $x$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.constPt`.

**Definition 5.1.4 (Infinitesimal rigidity).** Let $R$ be an $o$-algebra and $t$ a theta level object over $\operatorname{Spec} R$. We say $t$ is *infinitesimally rigid* if the following holds. Let $x : \operatorname{Spec} \mathbb{C}[\varepsilon] \to \operatorname{Spec} R$ have the same image in $\operatorname{Spec} o$ as its constant point $\bar x$, and let $t'$ be a theta level object over $\operatorname{Spec} \mathbb{C}[\varepsilon]$ with maps $t' \to t$ over $x$ and over $\bar x$. Then $x = \bar x$.

In words: a tangent vector of $\operatorname{Spec} R$ along which $t$ is constant is zero. A fine moduli space has this property, since two maps to it that classify the same object coincide.

Now fix the complex side. Let $t_0$ be a theta level object over $\operatorname{Spec} \mathbb{C}$, with abelian variety $A_0$ of dimension $g$, and let $u : \mathbb{C}^g \to A_0(\mathbb{C})$ be a uniformization with lattice $\Lambda$. Let $H$ be a complex $g \times g$ matrix and $\chi : \Lambda \to \mathbb{C}$.

**Definition 5.1.5 (Good uniformization).** The pair $(H, \chi)$ makes $u$ *good* if $L_0$ is the line bundle of the Appell-Humbert data $(H, \chi)$ for $u$; tangent vectors of $A_0$ at the origin correspond bijectively to differentials of $u$; every endomorphism $f$ of the group $A_0$ lifts to a $\mathbb{C}$-linear map $F$ of $\mathbb{C}^g$ with $u(F z) = f(u(z))$; and every theta function of level $n$ for $(H, \chi)$ is a section of $L_0^n$.

Lean: `GlobalTheory.KS.GoodU`.

We write $\langle z, w \rangle_H$ for the hermitian form with matrix $H$.

**Definition 5.1.6 (Kodaira-Spencer relation).** Let $p : X \to \operatorname{Spec} R$ be a scheme over $R$, let $m : A_0 \to X$ be a morphism, let $D : R \to \mathbb{C}$ be a function and let $\Theta$ be a complex $g \times g$ matrix. A *Kodaira-Spencer relation* for $(D, \Theta)$ is a family $s = (s_z)_{z \in \mathbb{C}^g}$ with the following properties.

1. Each $s_z$ is a point derivation of $\mathcal{O}_X$ at the point $m(u(z))$: on each open $W$ containing it, $s_z$ is additive, satisfies the Leibniz rule $s_z(f f') = f(m u z)\, s_z(f') + f'(m u z)\, s_z(f)$ and is compatible with restriction.
2. On functions from the base, $s_z(p^* r) = D(r)$ for every $r \in R$.
3. For each open $W$ and $f \in \mathcal{O}_X(W)$, the function $z \mapsto s_z(f)$ is holomorphic on the set of $z$ with $m(u(z)) \in W$.
4. For each $l \in \Lambda$, $s_{z + l}(f) = s_z(f) + d(f \circ m \circ u)_z\bigl(\Theta \bar l\bigr)$.

Lean: `GlobalTheory.KS.KSRel`, `GlobalTheory.KS.PtDer`.

The matrix $\Theta$ is the Kodaira-Spencer class. Over $\mathbb{C}[\varepsilon]$ the lattice moves to $\{l + \varepsilon\, \Theta \bar l\}$, and a lift of $D$ along the fibre can be periodic only up to the derivative in the direction $\Theta \bar l$. The class $\Theta$ is the antilinear map $\bar z \mapsto \Theta \bar z$, from the antiholomorphic tangent space $H^1(A_0, \mathcal{O})$ to the tangent space $H^0(A_0, T)$, as in the classical description of the Kodaira-Spencer map of a family of complex tori.

**Definition 5.1.7 (Symmetric and commuting classes).** A matrix $\Theta$ is *symmetric for* $H$ if $\langle \Theta \bar z, w \rangle_H = \langle \Theta \bar w, z \rangle_H$ for all $z, w \in \mathbb{C}^g$. It *commutes with* a map $F$ of $\mathbb{C}^g$ if $F(\Theta \bar z) = \Theta\, \overline{F z}$ for all $z$.

Lean: `GlobalTheory.KS.IsSymm`, `GlobalTheory.KS.Comm`.

For the principal polarization the symmetric classes are the classical ones: in a basis where $H$ is the identity, $\Theta$ is symmetric for $H$ exactly when $\Theta$ is a symmetric matrix. This is the condition that cuts the tangent space of deformations of $A_0$ down to $\operatorname{Sym}^2 \operatorname{Lie}(A_0)$.

**Theorem 5.1.8 (The kernel of the Kodaira-Spencer map).** Assume the laws, the second laws and the uniformization theorem. Let $o$ carry a base of level $k$, let $R$ be an $o$-algebra with a map $R \to \mathbb{C}$ compatible with a map $o \to \mathbb{C}$, and let $t$ be an infinitesimally rigid theta level object over $\operatorname{Spec} R$. Let $t_0$ be a theta level object over $\operatorname{Spec} \mathbb{C}$, with a uniformization $u$ made good by $(H, \chi)$, and let $m : A_0 \to A$ be a map of theta level objects $t_0 \to t$ over $\operatorname{Spec} \mathbb{C} \to \operatorname{Spec} R$. Let $D$ be an $o$-[[Derivation|3J89REV9WQ]] $R \to \mathbb{C}$. If $D$ has a Kodaira-Spencer relation with class $\Theta = 0$ along $m$, then $D = 0$.

Lean: `GlobalTheory.KS.KerZero.derivation_eq_zero_of_ks_zero` (also `GlobalTheory.T.derivation_eq_zero_of_kodairaSpencer_zero`, a second name).

*Proof.* The derivation $D$ gives the ring map $R \to \mathbb{C}[\varepsilon]$, $r \mapsto r + D(r)\varepsilon$, so a point $x : \operatorname{Spec} \mathbb{C}[\varepsilon] \to \operatorname{Spec} R$ that reduces to the given complex point. Since $D$ vanishes on $o$, $x$ and $\bar x$ have the same image in $\operatorname{Spec} o$. Pull $t$ back along $x$ to a theta level object $t'$ over $\mathbb{C}[\varepsilon]$, with its map $t' \to t$ over $x$. The map $m$ factors through the special fibre of $t'$, and the factorization $j : A_0 \to A'$ is again a map of theta level objects, since the line bundle, the level points and the endomorphisms are all pulled back from $t$. Now use $\Theta = 0$. Then condition 4 says that each $s_z(f)$ is periodic in $z$, so the $s_z$ descend to a holomorphic family of point derivations along $A_0$ that lifts $D$. By the uniformization theorem and the laws this family splits $A'$: there is a retraction $\rho : A' \to A_0$ over $\operatorname{Spec} \mathbb{C}[\varepsilon] \to \operatorname{Spec} \mathbb{C}$ that identifies $A'$ with the constant family $A_0 \times \mathbb{C}[\varepsilon]$, with $\rho \circ j = 1$. The same three facts show that the constant family, with the pulled back line bundle, level points and endomorphisms, is the pullback of $t$ along $\bar x$. Composing the identifications gives maps $t' \to t$ over both $x$ and $\bar x$. Infinitesimal rigidity gives $x = \bar x$, that is $D(r)\varepsilon = 0$ for all $r$, so $D = 0$. $\square$

**Theorem 5.1.9 (Tangent vectors inject into symmetric antilinear classes).** Assume the laws, the second laws and the uniformization theorem. Let $o$ carry a base of level $k$, let $R$ be an $o$-algebra with a map $R \to \mathbb{C}$ compatible with a map $o \to \mathbb{C}$, and let $t$ be an infinitesimally rigid theta level object over $\operatorname{Spec} R$. Then there are a theta level object $t_0$ over $\operatorname{Spec} \mathbb{C}$, a map $m : t_0 \to t$ over $\operatorname{Spec} \mathbb{C} \to \operatorname{Spec} R$, a uniformization $u$ of $A_0$ made good by some $(H, \chi)$, and a $\mathbb{C}$-linear map
$$\kappa : \operatorname{Der}_o(R, \mathbb{C}) \to M_g(\mathbb{C})$$
with these properties:

1. $\kappa$ is injective;
2. every $\kappa(D)$ is symmetric for $H$;
3. let $f$ be an endomorphism of $A$, $f_0$ an endomorphism of $A_0$ with $m \circ f_0 = f \circ m$, and $F$ a $\mathbb{C}$-linear map of $\mathbb{C}^g$ with $u(F z) = f_0(u(z))$ for all $z$; then every $\kappa(D)$ commutes with $F$.

Lean: `GlobalTheory.KS.tangent_injects_symm_antilinear` (also `GlobalTheory.T.tangent_injects_symmetric_antilinear_commuting`, a second name).

*Proof.* Let $t_0$ be the pullback of $t$ to the complex point, with its map $m$. The uniformization theorem gives a good uniformization $u$ of $A_0$ with data $(H, \chi)$. The family $A$ is smooth over $R$, so each derivation $D$ lifts along the fibre to a family of point derivations as in the Kodaira-Spencer relation, and the failure of periodicity is the derivative in a direction $\Theta \bar l$ that is linear in $D$. This defines the $\mathbb{C}$-linear map $\kappa$, with a relation of class $\kappa(D)$ for each $D$. If $\kappa(D) = 0$, then $D = 0$ by [the theorem on the kernel](/entry/derivation-eq-zero-of-ks-zero/), so $\kappa$ is injective. The line bundle $L$ deforms with $A$ along $D$, because it is defined over all of $\operatorname{Spec} R$. A deformation of the lattice that carries a deformation of the Appell-Humbert form keeps the form hermitian, and to first order this says that $\kappa(D)$ is symmetric for $H$. In the same way every endomorphism $f$ of $A$ is defined over $R$, so its lift $F$ maps the deformed lattice into itself to first order, and this is the relation $F(\kappa(D) \bar z) = \kappa(D)\, \overline{F z}$. $\square$

**Remark 5.1.10.** In the classical language, $\kappa$ is the Kodaira-Spencer map of [the background](/learn/abelian-varieties/#the-kodaira-spencer-map) at one point, written as a map into antilinear maps $\operatorname{Lie}(A_0) \to \operatorname{Lie}(A_0)$. The theorem says that a family with infinitesimally rigid objects has injective Kodaira-Spencer map, with values in the symmetric and endomorphism-compatible part.

**Remark 5.1.11 (Formalization).** The laws are `Out.Laws`, the second laws are `Out.Laws2` and the uniformization theorem is `ThetaUnifAV`; they are hypotheses of both theorems. In the theorem on the kernel the complex point $s_0 : \operatorname{Spec} \mathbb{C} \to \operatorname{Spec} o$ of $t_0$ is arbitrary; only the map $m$ ties $t_0$ to $t$. The hermitian form `hermForm`, the uniformization structure `HolUnif`, the Appell-Humbert condition `IsAH` and the predicates `IsTangent`, `IsDiff`, `IsThetaFn`, `IsFnPow` were not unfolded. The proof of the kernel theorem runs through `T.exists_thetaLevelAbelianScheme_pullback`, `T.exists_isConst_of_ksRel_zero'`, `T.thetaObject_constantFamily_dualNumbers_isPullback` and `T.thetaLevelPullback_id_comp_cancel` ([DerivationEqZeroOfKodairaSpencerZero.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/DerivationEqZeroOfKodairaSpencerZero.lean#L40)); the injection theorem runs through `exists_goodUniformisation_kodairaSpencer`, `kodairaSpencer_matrix_linear_in_derivation`, `kodairaSpencer_class_isSymm_of_lift` and `kodairaSpencer_commutes_with_endomorphism` ([TangentInjectsSymmetricAntilinearCommuting.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/TangentInjectsSymmetricAntilinearCommuting.lean#L21)). We followed the statements of these lemmas, not their proofs, so the proofs above give the shape of the argument. The second names are proved by a `first | exact … | …` block under a raised heartbeat limit.
