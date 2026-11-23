---
title: A semi-abelian group scheme on the closure
decls:
  - GlobalTheory.T.exists_semiAbelian_split_cubical_extension_closure
  - GlobalTheory.ZJ.Assembly.exists_law_splitAll_cubical
  - GlobalTheory.T.exists_semiAbelian_groupScheme_cubical_bundle_closure
  - GlobalTheory.ClosureGroup.exists_pre
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A semi-abelian group scheme on the closure

[The previous section](/entry/base-facts-has-geo-exists-clos/) gave a closure $Q$ of the abelian scheme $A$ over $U_0$ and an extension of $Q$ whose core $C$ has tests, independence, fibres and charts. In this section we put a group law on the group part $G_Q$ of the closure, show that $G_Q$ is a semi-abelian scheme over $Z$ with split fibres, and extend the polarisation of $A$ to a rigidified cubical line bundle on $G_Q$ that has theta sections near every point. The result is a *pre-extension* of $\rho$, and it is the second step of [the extension of a theta-level abelian scheme](/entry/zh-geo/). We keep the notation of the previous section; for the cube see [the theorem of the cube](/learn/abelian-varieties/#the-theorem-of-the-cube) in Volume 1.

### Group laws, theta data and cubical maps

Let $C$ be a core, with base $Z$, open set $U \subset Z$, abelian scheme $A$ over $U$ of relative dimension $g$, open set $G \subset P$ with structure map $G \to Z$, map $a : A \to G$ and section $e$.

**Definition 6.11.1 (Group law on a core).** A *group law* on $C$ is a structure of commutative group scheme on $G \to Z$ that is smooth of relative dimension $g$, has unit section $e$, makes $a$ a cartesian map of group schemes over $U \subset Z$, and makes the map $H \to G$ of every test of $C$ a cartesian map of group schemes over the point of the test.

Lean: `GlobalTheory.ZJ.Core.Law`.

A group scheme $G$ over $Z$ is *semi-abelian* if it is commutative, smooth, separated, quasi-compact and geometrically connected, and each geometric fibre is an extension of an abelian variety by a torus. It is *split everywhere* if for each point $z \in Z$ the fibre over the residue field of $z$ is an extension of an abelian variety by a split torus. A *rigidified line bundle* on $G$ is a line bundle $\mathcal{L}$ with a generator of $e^* \mathcal{L}$; a *cubical structure* on it is a generator of the cube $\Theta(\mathcal{L})$ on $G^3$ that is trivial on the three faces, symmetric under the swaps and satisfies the cocycle condition. It is *symmetric* if $\mathcal{L} \cong [-1]^* \mathcal{L}$ by an isomorphism that respects the rigidification.

**Definition 6.11.2 (Cubical map).** For group schemes $G'$ over $S'$ and $G$ over $S$, a *cubical map* $m : G' \to G$ is a map $F : G' \to G$ with a map of bases $S' \to S$ and a map $G'^3 \to G^3$ that commute with the unit sections and with all partial sums of three points. If $c'$ and $c$ are cubical structures on $\mathcal{L}'$ and $\mathcal{L}$, then $m$ *pulls $c$ back to $c'$* if there is an isomorphism $\mathcal{L}' \cong F^* \mathcal{L}$ that carries the rigidification of $\mathcal{L}'$ to the pullback of that of $\mathcal{L}$ and the cubical generator $c'$ to the pullback of $c$.

Lean: `ReciprocityTheory.ChartRestriction.G.Semi.CubeMap` (also `ReciprocityTheory.ChartRestriction.G.Semi.CubeMap.IsPullCubical`, pulling back).

**Definition 6.11.3 (Theta data on a core).** *Theta data* $T$ on $C$ consist of a rigidified line bundle $\mathcal{L}$ on $A$ with a cubical structure, a section $\theta$ of $\mathcal{L}$, an integer $m$ that is a unit on $Z$, a line bundle $\mathcal{O}_1$ on $G$ with a section $s$, and an isomorphism $[m]^* \mathcal{L} \cong a^* \mathcal{O}_1$ that carries $\theta \circ [m]$ to $s \circ a$, such that over each closed point of $Z$ there is a point of $G$ where $s$ does not vanish. An *extension* of $T$ to a test $(V, H)$ of $C$ is a rigidified line bundle on $H$ that is isomorphic to the pullback of $\mathcal{L}$ on the generic fibre, with a section $\theta_H$ that matches $\theta$ there and does not vanish at some point of the special fibre.

Lean: `GlobalTheory.ZJ.Core.Theta` (also `GlobalTheory.ZJ.Core.Theta.Ext`, extensions to tests).

**Definition 6.11.4 (Torsion sections and few zeros).** Let $n \geq 1$. The core has *torsion sections of order $n$* if each closed point $z$ has an open neighbourhood $N$ with this property: for every test at an $\mathcal{O}_p$-point centred at $z$, every point $x$ of $N$ over the residue field that lies under the reduction of the test point, and every $n$-torsion point $c$ of the special fibre of $H$, there is a section $h : N \to G$ over $N$ with $x^* h$ equal to the image of $c$. Theta data $T$ have *few zeros of order $n$* if, for every test, every extension of $T$ to it and every point $c$ of the special fibre of $H$, fewer than one sixth of the $n$-torsion points $h$ of the special fibre have $\theta_H$ vanishing at $c + h$.

Lean: `GlobalTheory.ZJ.Core.TorsSec` (also `GlobalTheory.ZJ.Core.Theta.Few`, few zeros).

### Inputs on the core

The inputs below are proved elsewhere in the Lean development. In the last two, $S$ is an integral, locally noetherian, normal scheme, $j : U \to S$ is the inclusion of a nonempty open set, and $G$ is a smooth commutative group scheme over $S$ with connected geometric fibres.

**Theorem 6.11.5 (A group law).** If the core $C$ has tests and independence, then $C$ has a group law.

Lean: `GlobalTheory.ZJ.Core.nonempty_law_of_hasTests_of_indep`.

**Theorem 6.11.6 (Semi-abelian and split).** For a group law on a core with tests and charts, $G$ is split everywhere and semi-abelian.

Lean: `GlobalTheory.ZJ.FibreSplit.splitAll_and_isSemiAbelian`.

**Theorem 6.11.7 (Extension of the line bundle).** Assume the extension statement for semi-abelian schemes, the statement on multiplication by $n$, and that $[n]$ is surjective on abelian varieties over algebraically closed fields in which $n \neq 0$. Let $C$ have a group law for which $G$ is semi-abelian, tests and torsion sections of order $n$, and let $T$ have few zeros of order $n$. Then there is a line bundle $\mathcal{M}$ on $G$ with $a^* \mathcal{M} \cong \mathcal{L}$ such that each $z \in Z$ has a neighbourhood $N$ and a section of $\mathcal{M}$ over $G_N$ that does not vanish at some point over each $z' \in N$.

Lean: `GlobalTheory.T.exists_lineBundle_extension_thetaSection_semiAbelian`.

**Theorem 6.11.8 (Cubical extension).** Let $a : A \to G$ be a cartesian map of group schemes over $j$, let $\mathcal{L}$ be a rigidified line bundle on $A$ with a cubical structure $c$, and let $\mathcal{M}$ be a line bundle on $G$ with $a^* \mathcal{M} \cong \mathcal{L}$. Then there are a rigidified line bundle $\mathcal{L}'$ on $G$ with a cubical structure $c'$ and a cubical map $m$ with $F = a$ over $j$ that pulls $c'$ back to $c$, and $\mathcal{L}'$ is symmetric if $\mathcal{L}$ is.

Lean: `GlobalTheory.NormalCubeExt.exists_cubical_extension`.

**Theorem 6.11.9 (Isomorphisms extend).** Let $p : H \to S$ be smooth with geometrically integral fibres and a section $e$, and let $H_U$ be the part over $U$. Let $\mathcal{L}$ and $\mathcal{M}$ be line bundles on $H$ with $\mathcal{L}|_{H_U} \cong \mathcal{M}|_{H_U}$. If also $e^* \mathcal{L} \cong e^* \mathcal{M}$, then $\mathcal{L} \cong \mathcal{M}$. In any case each point of $S$ has a neighbourhood $N$ with $\mathcal{L}|_{p^{-1}N} \cong \mathcal{M}|_{p^{-1}N}$.

Lean: `GlobalTheory.T.lineBundleIso_extend_of_normal_base`.

We also use that $Z$ is noetherian and $a$ is cartesian over $U$ (`GlobalTheory.ZJ.core_basic`), and that a smooth group scheme with connected geometric fibres is geometrically integral.

### A cubical extension on the core

**Lemma 6.11.10 (Sections along isomorphisms).** Let $p : H \to S$ and let $\mathcal{L}$, $\mathcal{M}$ be line bundles on $H$. Let $z \in S$. If $\mathcal{L} \cong \mathcal{M}$ over $p^{-1} N_1$ for a neighbourhood $N_1$ of $z$, and $\mathcal{M}$ has a section over $p^{-1} N_2$ for a neighbourhood $N_2$ that does not vanish at some point over each point of $N_2$, then $\mathcal{L}$ has such a section over $p^{-1}(N_1 \cap N_2)$.

Lean: `GlobalTheory.ZJ.Assembly.exists_sec_fibres`.

*Proof.* Restrict the isomorphism and the section to $p^{-1}(N_1 \cap N_2)$. The section of $\mathcal{M}$ gives a section of $\mathcal{L}$ through the isomorphism, and this section does not vanish where the first does not, since the isomorphism is given by units. $\square$

**Theorem 6.11.11 (Semi-abelian cubical extension).** Assume the first bundle of laws. Let $C$ be a core with tests, independence, charts and torsion sections of order $n$, and let $T$ be theta data on $C$ with few zeros of order $n$. Then there is a group law on $C$ such that $G$ is split everywhere and semi-abelian, and there are a rigidified line bundle $\mathcal{L}'$ on $G$ with a cubical structure $c'$ and a cubical map $m$ with $F = a$ over $U \subset Z$, such that:

1. $m$ pulls $c'$ back to the cubical structure of $T$;
2. if the line bundle $\mathcal{L}$ of $T$ is symmetric, so is $\mathcal{L}'$;
3. each $z \in Z$ has a neighbourhood $N$ and a section of $\mathcal{L}'$ over $G_N$ that does not vanish at some point over each $z' \in N$;
4. each $z \in Z$ has a neighbourhood $N$ over which $\mathcal{O}_1 \cong [m]^* \mathcal{L}'$ on $G$.

Lean: `GlobalTheory.T.exists_semiAbelian_split_cubical_extension_closure` (also `GlobalTheory.ZJ.Assembly.exists_law_splitAll_cubical`, a second name).

*Proof.* The theorem on a group law gives a law on $C$, and the theorem on semi-abelian schemes shows that $G$ is split everywhere and semi-abelian. The extension of the line bundle, with the laws on extension and on $[n]$ and the surjectivity of $[n]$, gives $\mathcal{M}$ on $G$ with $a^* \mathcal{M} \cong \mathcal{L}$ and local sections. Since $G$ is semi-abelian, it is smooth with connected geometric fibres, so it is geometrically integral. The cubical extension, applied to $\mathcal{M}$, gives $\mathcal{L}'$, $c'$ and $m$ with properties 1 and 2. Property 1 gives $\mathcal{L} \cong a^* \mathcal{L}'$.

For property 3, $a^* \mathcal{L}' \cong \mathcal{L} \cong a^* \mathcal{M}$, and $a$ is the inclusion of the part of $G$ over $U$. By the theorem that isomorphisms extend, $\mathcal{L}' \cong \mathcal{M}$ near each fibre, and the lemma moves the sections of $\mathcal{M}$ to $\mathcal{L}'$.

For property 4, the theta data give $a^* \mathcal{O}_1 \cong [m]^* \mathcal{L}$. Since $a$ is a cartesian map of group schemes, $[m] \circ a = a \circ [m]$, so $[m]^* \mathcal{L} \cong [m]^* a^* \mathcal{L}' = a^* [m]^* \mathcal{L}'$. So $\mathcal{O}_1$ and $[m]^* \mathcal{L}'$ are isomorphic on the part over $U$, and the theorem that isomorphisms extend makes them isomorphic near each fibre. $\square$

### The pre-extension

**Definition 6.11.12 (Pre-extension).** A *pre-extension* of $\rho$ over $(M, U_0)$ consists of a map $u_0 : U_0 \to \operatorname{Spec} R$ that is the identity at the generic point; a semi-abelian scheme $G$ over $Z$ of relative dimension $g$, quasi-projective over $o$; a cartesian map of group schemes $u_0^* A \to G$ over $U_0$; a symmetric rigidified line bundle $\mathcal{L}'$ on $G$ with a cubical structure; an isomorphism of its pullback to $u_0^* A$ with the pullback of $L$ that matches the rigidifications; and splitting of the fibres of $G$ over every point. It has *local theta sections* if each $z \in Z$ has a neighbourhood $N$ and a section of $\mathcal{L}'$ over $G_N$ that does not vanish at some point over each $z' \in N$.

Lean: `GlobalTheory.ZH.ZHPre` (also `GlobalTheory.ZH.ZHPre.LocTheta`, local theta sections).

**Theorem 6.11.13 (Inputs on theta data).** Assume the first two bundles of laws and the uniformisation statement. If $T$ is theta data on a core whose line bundle is relatively ample, has trivial group $K(\mathcal{L})$, is symmetric and satisfies the symmetry hypothesis, and $N \geq 4$ and $n$ are integers with $n$ a unit on $Z$ and $6 N^g g! < n^2$, then $T$ has few zeros of order $n$. These four conditions pass from $L$ to every line bundle isomorphic to its pullback along a cartesian map of abelian schemes.

Lean: `GlobalTheory.ZJ.theta_few` (also `GlobalTheory.pol_pull`, relative ampleness and $K$; `GlobalTheory.SymBaseChange.hypS_baseChange`, the symmetry hypothesis).

**Theorem 6.11.14 (Group scheme on the closure).** Assume the first two bundles of laws and the uniformisation statement. Let $S$ be a big theta system over an arithmetic base with a realisation $\rho$, let $Q$ be a closure of $\rho$ over $(M, U_0, E)$, and let $Q$ have an extension whose core has tests, independence, charts and torsion sections of order $rN$. Assume there are theta data $T$ on the core whose line bundle is isomorphic to the pullback of $L$. Then there is a pre-extension of $\rho$ with local theta sections whose group scheme is $G_Q$ over $Z$, with the same $u_0$ and the same map $u_0^* A \to G_Q$, and the core has a group law.

Lean: `GlobalTheory.T.exists_semiAbelian_groupScheme_cubical_bundle_closure` (also `GlobalTheory.ClosureGroup.exists_pre`, a second name).

*Proof.* The pullback of $L$ is relatively ample with trivial $K$, it is symmetric, and it satisfies the symmetry hypothesis, because $L$ is and $u_0^* A \to A$ is cartesian. These pass to the line bundle of $T$. Since $N = n^{2k}$ with $n \geq 3$ and $k \geq 2$, we have $N \geq 4$. The integer $rN$ is a unit in $o$, hence on $Z$. Bigness gives $6 N^g g! < rN \leq (rN)^2$. So $T$ has few zeros of order $rN$. The semi-abelian cubical extension with $n = rN$ gives a group law, splitting, semi-abelianness, $\mathcal{L}'$, $c'$ and $m$ with properties 1 to 3.

Property 1 gives $\mathcal{L} \cong a^* \mathcal{L}'$, so the pullback of $L$ is isomorphic to the pullback of $\mathcal{L}'$. On both sides the zero sections commute with the maps of the cartesian squares. A gluing argument with units on the base rescales this isomorphism so that it matches the rigidifications of $L$ and $\mathcal{L}'$ at every point of the zero section. The line bundle of $T$ is symmetric, so $\mathcal{L}'$ is symmetric by property 2. The group part is quasi-projective over $o$, since it is open in $P$, which is projective over $o$, and the inclusion is quasi-compact. These data form a pre-extension, and property 3 is the condition on local theta sections. $\square$

**Remark 6.11.15 (Formalization).** The cubical extension on the core is proved in [ExistsSemiAbelianSplitCubicalExtensionClosure.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsSemiAbelianSplitCubicalExtensionClosure.lean#L76), with the lemma on sections at line 52, and the group scheme on the closure in [ExistsSemiAbelianGroupSchemeCubicalBundleClosure.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsSemiAbelianGroupSchemeCubicalBundleClosure.lean#L117). The rescaling is the local lemma `exists_rescale` (line 31) and symmetry along a pullback is `isSymmetric_of_pull` (line 92). Both statement forms are `first | exact ...` blocks with `maxHeartbeats 1000000`. The proof of the group scheme on the closure discards property 4 of the cubical extension (line 137), so the isomorphism $\mathcal{O}_1 \cong [m]^* \mathcal{L}'$ is not used, and the group law in its conclusion is the law of the pre-extension stated again. We did not unfold `SplitExt.IsGt`, `TorusExtension`, `Out.RelAmple`, `Out.KTriv`, `HypS`, the five bundles of laws or the uniformisation statement `ThmUSt`.
