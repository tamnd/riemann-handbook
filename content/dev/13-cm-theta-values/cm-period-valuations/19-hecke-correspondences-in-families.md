---
title: Hecke correspondences in families
decls:
  - GlobalTheory.HkFam.heckeInFamilies
  - GlobalTheory.T.nonempty_heckeCorrespondenceScheme
  - GlobalTheory.HkFam.corr_nonempty
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hecke correspondences in families

This section constructs the Hecke correspondence of a prime $\mathfrak{P}$ on a moduli space of abelian schemes with an action of a CM field. Its points are pairs of an abelian scheme and a Hecke subgroup, and the second projection sends such a pair to the quotient. We show that the correspondence exists, that its second projection is finite and étale, and that its geometric points are the Hecke subgroups of the geometric fibres. The result is used in [the Hecke sums](/entry/exists-sum/) of Volume 8.

### Setup

Let $E$ be a CM field with complex conjugation $x \mapsto \bar{x}$, $H$ a host over $E$, $D$ a datum with signature $(D.p, D.q)$ and $1 \le D.p + D.q$, and $l$ a level with integer $M'$. Let $X$ be a moduli space for $(D, l)$, with structure map $s$ to the base and universal object $A^{\mathrm{univ}}$. An *object* over a scheme $S$ over the base has an abelian scheme $A$ over $S$ with an action of $\mathcal{O}_E$, a line bundle $L$ and level structures $\eta$ and $\eta_A$; its other data are not unfolded here.

**Definition 5.19.1 (Admitted prime).** A pair $(\mathfrak{P}, p)$ is *admitted* for $l$ if $\mathfrak{P}$ is a maximal ideal of $\mathcal{O}_E$, $\mathfrak{P} + \bar{\mathfrak{P}} = \mathcal{O}_E$, $p$ is a prime number in $\mathfrak{P}$, and $p$ does not divide $M'$.

For an ideal $J$ of $\mathcal{O}_E$, write $A[J]$ for the points killed by every element of $J$.

**Definition 5.19.2 (Hecke subgroup).** Let $A$ be an object over an algebraically closed field and $i \ge 0$. A subgroup $C$ of $A$ is a *Hecke subgroup* for $(\mathfrak{P}, p, i)$ if:
1. $C$ is stable under $\mathcal{O}_E$;
2. $A[J] \subseteq C$ for every ideal $J$ with $J \mathfrak{P} = (p)$;
3. $C \subseteq A[p \bar{\mathfrak{P}}]$;
4. $C$ is isotropic for the Weil pairing of $L$ at $p^2$;
5. $|C| = p^{2 \cdot ([E : \mathbb{Q}]/2) \cdot (D.p + D.q)}$;
6. $|A[p]| = |C \cap A[p]| \cdot N(\mathfrak{P})^i$.

A set $K$ of points of an object $A$ over $S$ is a *Hecke set* if at every geometric point $x$ of $S$ the points of $A_x$ with values in $K$ form a Hecke subgroup. It is *étale* if it is the image of a closed immersion of a finite étale $S$-scheme.

**Definition 5.19.3 (Isogeny of objects).** Let $A$ and $A'$ be objects over $S$. An *isogeny* $\psi : A \to A'$ is a homomorphism that is finite, étale, surjective and $\mathcal{O}_E$-linear, with $L^{\otimes p^2} \cong \psi^* L'$, and with $\psi \circ \eta(p' a) = \eta'(a)$ and $\psi \circ \eta_A(p' a) = \eta'_A(a)$ whenever $p p' \equiv 1 \bmod M'$. Its *kernel* is the set $K$ such that at every geometric point, a point lies in $\ker \psi$ exactly when its values lie in $K$. It is a *Hecke isogeny* if it has a kernel that is a Hecke set.

**Definition 5.19.4 (Hecke correspondence).** A *Hecke kernel scheme* for $(\mathfrak{P}, p, i)$ is a scheme $H_k$ with a finite étale map $\pi_1 : H_k \to X$, an object $A_1$ over $H_k$ mapped to $A^{\mathrm{univ}}$ over $\pi_1$, and an étale Hecke set $K$ of $A_1$, with this property: for every reduced $S$, every object $A$ over $S$ and every étale Hecke set $K'$ of $A$ there is a unique $h : S \to H_k$ over the base such that $A$ maps to $A_1$ over $h$ and $K'$ is the preimage of $K$. A *Hecke correspondence* adds a map $\pi_2 : H_k \to X$ over the base, an object $A_2$ mapped to $A^{\mathrm{univ}}$ over $\pi_2$, and an isogeny $\psi : A_1 \to A_2$ with kernel $K$, with this property: for every reduced $S$ and every Hecke isogeny $\psi' : A \to A'$ of objects over $S$, there is a unique $h : S \to H_k$ over the base with maps $A \to A_1$ and $A' \to A_2$ over $h$ that intertwine $\psi'$ and $\psi$.

A geometric point $z$ of $H_k$ *carries* $(y, C)$ if $\pi_1(z) = y$ and the points of $A_{1, z}$ with values in $K$ map onto $C$. A geometric point $y''$ is a *quotient point* of $(y, C)$ if $y''$ and $y$ lie over the same point of the base and there is a surjective $\mathcal{O}_E$-linear map $A^{\mathrm{univ}}_y \to A^{\mathrm{univ}}_{y''}$ with kernel $C$ that respects the level structures as above and takes Weil pairings of order $n$ prime to $p$ with value $c$ to Weil pairings with value $c^{p^2}$.

### The theorems

**Theorem 5.19.5 (Hecke correspondence exists).** Let $1 \le D.p + D.q$ and let $(\mathfrak{P}, p)$ be admitted for $l$. Then for every $i$ there is a Hecke correspondence for $(\mathfrak{P}, p, i)$ on $X$.

Lean: `GlobalTheory.HkFam.corr_nonempty` (also `GlobalTheory.T.nonempty_heckeCorrespondenceScheme`, a second name)

*Proof.* **The kernel scheme.** A lemma on Hecke kernel schemes gives a Hecke kernel scheme $(H_k, \pi_1, A_1, K)$, together with a property of its universal object over reduced bases. The scheme $H_k$ is reduced: $X$ is smooth over the base, $\pi_1$ is étale, so $H_k$ is smooth over a field, and a smooth scheme over a field is reduced.

**The quotient.** By a lemma on étale level structures, there is an étale surjective cover $S' \to H_k$ over which the pullback of $K$ is a union of a finite list of sections, distinct at every geometric point and killed by a fixed integer. Hecke sets are stable under pullback, so this list is a Hecke set over $S'$. A lemma on quotients over smooth bases gives the quotient of the pullback of $A_1$ by the listed kernel. A descent lemma along the étale surjective cover then gives an object $A_2$ over $H_k$ and an isogeny $\psi : A_1 \to A_2$ with kernel $K$. The moduli property of $X$ gives $\pi_2 : H_k \to X$ with $A_2$ mapped to $A^{\mathrm{univ}}$ over $\pi_2$.

**Universality.** Let $S$ be reduced and $\psi' : A \to A'$ a Hecke isogeny with kernel $K'$. The kernel of an isogeny is étale, so $K'$ is an étale Hecke set. The property of $H_k$ gives a unique $h : S \to H_k$ with $A \to A_1$ over $h$ and $K'$ the preimage of $K$. Pull $A_2$ back along $h$ to $A_3$, and pull $\psi$ back to an isogeny $\psi_3 : A \to A_3$, whose kernel is again the preimage of $K$, that is $K'$. Every point with values in a Hecke set is killed by $p^2$, by condition 3. So a lemma on quotients with the same kernel over a reduced base gives an isomorphism $A' \cong A_3$ that intertwines $\psi'$ and $\psi_3$. This gives the map $A' \to A_2$ over $h$. For uniqueness, let $h'$ be another map with intertwining maps. The pullback of $\psi$ along $h'$ has kernel the preimage of $K$. A kernel is determined by the isogeny, so this preimage is $K'$. The uniqueness for $H_k$ gives $h' = h$. $\square$

**Theorem 5.19.6 (Hecke correspondences in families).** Let $1 \le D.p + D.q$ and let $(\mathfrak{P}, p)$ be admitted for $l$. Then:
1. there is a Hecke correspondence $Z$ for $(\mathfrak{P}, p, i)$ with $\pi_2$ finite and étale, with $\pi_1$ and $\pi_2$ surjective if $i \le D.p + D.q$, and such that for every geometric point $y$ of $X$ and every Hecke subgroup $C$ of $A^{\mathrm{univ}}_y$ there is exactly one geometric point $z$ of $H_k$ that carries $(y, C)$, and $\pi_2(z)$ is then a quotient point of $(y, C)$;
2. for every reduced $S$, every object $A$ over $S$ and every finite étale closed subgroup scheme $C \hookrightarrow A$ whose image is a Hecke set, there is a unique $f : S \to X$ over the base such that the pullback $A'$ of $A^{\mathrm{univ}}$ along $f$ receives an isogeny $\psi : A \to A'$ with $C = \ker \psi$, as a fibre product of $\psi$ with the unit section.

Lean: `GlobalTheory.HkFam.heckeInFamilies`

*Proof.* Part 2 is a lemma on Hecke quotients over reduced bases. For part 1, take $Z$ from the previous theorem. A lemma on the second projection gives that $\pi_2$ is finite and étale and that $\pi_2$ is surjective when $i \le D.p + D.q$. A lemma on the geometric points of the Hecke kernel scheme gives the unique carrying point, and that $\pi_1$ is surjective when $i \le D.p + D.q$. A last lemma shows that if $z$ carries $(y, C)$, then $\pi_2(z)$ is a quotient point of $(y, C)$. $\square$

These results are the moduli form of the Hecke correspondences of a Shimura variety of unitary type at a prime $\mathfrak{P}$ prime to its conjugate. The Lean statements are about schemes over the base of a fixed level, and they quantify over Hecke subgroups through conditions 1 to 6 rather than through lattices.

**Remark 5.19.7 (Formalization).** Several facts about the Lean code:
1. `GlobalTheory.T.nonempty_heckeCorrespondenceScheme` is a second name, proved by `first | exact @… | …` under `maxHeartbeats 1000000` (ModuliProofs/NonemptyHeckeCorrespondenceSchemeStatement.lean:12).
2. The definitions are in Definitions/ModuliSpaces/KerScheme.lean: admitted primes at line 11, Hecke sets at line 17, kernels `KerSet` at line 21, étale sets at line 24, isogenies `IsIsogT` and `IsIsog` at lines 31 and 36, Hecke isogenies at line 39, `KerScheme` at line 45, `Corr` at line 63, quotient points `PointQuot` at line 79 and `Carries` at line 93. The six conditions are `SAB.HeckeKer` (ReciprocityTheory/…/ToroidalCompactification/HeckeKer.lean:59). The statement is `GlobalTheory.HkFam.HeckeInFamilies` (Statements/HeckeInFamilies/HeckeInFamilies.lean:11).
3. Two short lemmas in the same file carry part of the universality step: `corr_kerSet_unique` (a kernel is unique, NonemptyHeckeCorrespondenceScheme.lean:25) and `corr_heckeSet_kill` (points with values in a Hecke set are killed by $p^2$, line 36). The proof of `corr_kerSet_unique` uses a geometric point through each point of the scheme.
4. In `corr_nonempty` the hypothesis $1 \le D.p + D.q$ is used only in the quotient lemma over smooth bases; the kernel scheme lemma does not take it (NonemptyHeckeCorrespondenceScheme.lean:61 and :71).
5. The lemmas on the kernel scheme, on étale level structures, on quotients, on descent and on the projections are second names in the namespace `GlobalTheory.T`. None of them is in the chapter outline, so they have no entry links, and they are not unfolded here.
