---
title: Period data of abelian schemes
decls:
  - GlobalTheory.AbelianPeriodDatum.main
  - GlobalTheory.T.exists_periodTowerDatum_of_abelianScheme_symmetricBundle
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Period data of abelian schemes

This section applies [the theorem on period data](/entry/period-datum-main/) to an abelian scheme $G$ over $\Lambda = A_{\mathrm{inf}}/(\xi^2)$ with a symmetric line bundle $\mathcal{P}$ on $G \times G$ that is a biextension. The bundle $\mathcal{P}$ plays the part of a Poincaré bundle composed with a polarization ([polarizations](/learn/abelian-varieties/#polarizations-and-zarhins-trick)). An action of a ring $O_0$ with involution on the base change $G'$ of $G$ to $\mathcal{O}$ is assumed to satisfy the Rosati condition for $\mathcal{P}$. The theorem gives a framed group for $G$, the action of $O_0$ on it, and a period datum with this action. It feeds the construction of Hodge-Tate data for polarized abelian schemes with multiplication by $O_0$, which the length bounds of [the unramified case](/entry/unramified-companion-chart-characters/) and [the split case](/entry/colength-bound-split-place-chart/) use.

We keep the notation of [the previous section](/entry/period-datum-main/): $C$, $v$, $\mathcal{O}$, $\varepsilon$, $\Lambda$ and the $A_{\mathrm{inf}}$ tower. For a scheme $X$ and a line bundle $\mathcal{L}$ on $X$, a *generator* of $\mathcal{L}$ is a nowhere vanishing global section, so $\mathcal{L}$ is trivial. For a group scheme $H$ and a line bundle $\mathcal{L}$ on $H$, let $\Theta(\mathcal{L})$ be the line bundle on $H^3$ of the theorem of the cube,
$$\Theta(\mathcal{L}) = \bigotimes_{I \subseteq \{1, 2, 3\}} m_I^* \mathcal{L}^{(-1)^{3 - |I|}},$$
where $m_I(x_1, x_2, x_3) = \sum_{i \in I} x_i$ (Mumford, *Abelian Varieties*, §6). A generator of $\Theta(\mathcal{L})$ is a cubical structure on $\mathcal{L}$.

**Theorem 4.2.1 (Period data of abelian schemes).** Let $G$ be an abelian scheme over $\Lambda$, smooth of relative dimension $g$. Let $\mathcal{P}$ be a line bundle on $G \times G$. Assume:

1. $\Theta(\mathcal{P})$ has a generator, where $\mathcal{P}$ is a line bundle on the group scheme $G \times G$;
2. the restrictions of $\mathcal{P}$ to $\{1\} \times G$ and to $G \times \{1\}$ have generators;
3. $\mathcal{P} \cong s^*\mathcal{P}$, where $s(x, y) = (y, x)$;
4. $[p] : G \to G$ is finite, flat and surjective.

Let $\mathcal{O} \to C$ and $\Lambda \to C$ be algebra maps that commute with $\Lambda \to \mathcal{O}$, and assume that $\mathcal{O}$ is the ring of integers of $v$ for the map $\mathcal{O} \to C$. Assume:

5. if $x \in G(C)$ and the restriction of $\mathcal{P}$ to $\{x\} \times G_C$ has a generator, then $x = 1$;
6. $\#G(C)[p] = p^{2g}$.

Let $G'$ be an abelian scheme over $\mathcal{O}$ and $\varphi : G' \to G$ a morphism that makes $G'$ the base change of $G$ as a group, with $\varphi \times \varphi$ on $G' \times G'$. Let $\mathcal{O}$ be a $\mathbb{Z}_p$-algebra, let $O_0$ be a commutative ring with an involutive automorphism $a \mapsto \bar a$, and let $a \mapsto [a]$ be an action of $O_0$ on $G'$ by endomorphisms of group schemes, with $[1] = 1$, $[ab] = [a][b]$ and $[a + b] = [a] + [b]$. Assume:

7. (Rosati condition) for each $a \in O_0$ the line bundle $\bigl(([a] \times 1)^* \mathcal{P}'\bigr) \otimes \bigl((1 \times [\bar a])^* \mathcal{P}'\bigr)^{-1}$ on $G' \times G'$ has a generator, where $\mathcal{P}' = (\varphi \times \varphi)^*\mathcal{P}$.

Then there are a framed group $\mathcal{B}$ over $\Lambda$, bijections $e_R : G_{\mathcal{B}}(R) \to G(R)$ for each local $\Lambda$-algebra $R$, additive and natural in $R$, and endomorphisms $\mathrm{Ad}(a)$ of $G_{\mathcal{B}}$ over $\mathcal{O}$-algebras with adjoints for the biextension, such that $\mathrm{Ad}(a)$ corresponds to $[a]$: if a point $x'$ of $G'$ over an $\mathcal{O}$-algebra $R$ lies over $e_R(x)$, then $[a]x'$ lies over $e_R(\mathrm{Ad}(a)x)$. There is also a period datum $D$ of $\mathcal{B}$ for $O_e = \mathbb{Z}_p \otimes O_0$, $\sigma = 1 \otimes \bar{\ }$ and $c_p = \zeta_p - 1$, with $P = 0$, $P_L = 0$, with $\mathrm{Ad}(a)$ acting on tangent vectors through $\rho_L(1 \otimes a)$, and with $\mathrm{Ad}(a)\tau_j(n) = \sum_k \bigl(\rho(1 \otimes a)_{kj} \bmod p^{n+1}\bigr)\tau_k(n)$.

Lean: `GlobalTheory.AbelianPeriodDatum.main` (also `GlobalTheory.T.exists_periodTowerDatum_of_abelianScheme_symmetricBundle`, a second name).

*Proof.* We check the hypotheses of [the theorem on period data](/entry/period-datum-main/). First, $\mathcal{P}$ is a biextension of $G \times G$ by $\mathbb{G}_m$. A cubical structure on a line bundle of $G \times G$ that is trivial on $\{1\} \times G$ and $G \times \{1\}$ gives the two partial group laws (hypotheses 1 and 2), as in the theorem of the cube. By hypothesis 3 the biextension is symmetric. From $G$, $\mathcal{P}$ and the symmetric biextension we build a framed group $\mathcal{B}$ with the bijections $e_R$, so that $G_{\mathcal{B}}(R)$ is $G(R)$ as a group and the biextension of $\mathcal{B}$ is the one given by $\mathcal{P}$; smoothness of relative dimension $g$ gives the tangent module of rank $g$. The Rosati condition (hypothesis 7) says that $[a]$ and $[\bar a]$ are adjoint for $\mathcal{P}'$. So $[a]$ gives an endomorphism $\mathrm{Ad}(a)$ of $G_{\mathcal{B}}$ over $\mathcal{O}$-algebras with adjoint $\mathrm{Ad}(a)^*$ coming from $[\bar a]$. Since $a \mapsto [a]$ is a ring action, $\mathrm{Ad}(a)^* = \mathrm{Ad}(\bar a)$, $\mathrm{Ad}(1) = 1$, and $\mathrm{Ad}$ is additive and multiplicative.

Next, the integral points. Since $[p]$ is finite and surjective and $\mathcal{O}$ is the ring of integers of $v$ in the algebraically closed field $C$, each point of $G(\mathcal{O})$ is $p$ times a point of $G(\mathcal{O})$, and each $p$-torsion point of $G(C)$ extends to a unique point of $G(\mathcal{O})$. So $G(\mathcal{O})$ is $p$-divisible and $\#G(\mathcal{O})[p] = \#G(C)[p] = p^{2g}$ by hypothesis 6. Last, the Weil pairing on $G(\mathcal{O})[p]$ is nondegenerate: if $e_p(x, y) = 1$ for all $y$, then the restriction of $\mathcal{P}$ to $\{x\} \times G$ descends through $[p]$ and is trivial on the geometric fibre, so $x = 1$ by hypothesis 5. Now [the theorem on period data](/entry/period-datum-main/) gives the period datum. $\square$

**Remark 4.2.2 (Formalization).** The theorem assumes two algebra structures on $\mathcal{O}$ over $C$: the one that makes $\mathcal{O}$ the ring of integers of $v$ in the construction of the tower, and a second one, with its own copy of the hypothesis that $\mathcal{O}$ is the ring of integers of $v$, used for the points over $C$. The statement does not say that they agree. The point count and the nondegeneracy use the second one. The second name is proved by `first | exact @GlobalTheory.AbelianPeriodDatum.main | ...` at [ExistsPeriodTowerDatumOfAbelianSchemeSymmetricBuStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/ExistsPeriodTowerDatumOfAbelianSchemeSymmetricBuStatement.lean#L21), with a raised heartbeat limit. The steps on the biextension, the framed group, the Rosati adjoint and the integral torsion are results of their own in the development; we have opened their statements, not their proofs.
