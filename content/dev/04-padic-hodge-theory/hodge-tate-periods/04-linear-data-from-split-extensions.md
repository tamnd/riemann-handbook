---
title: Linear data from split extensions
decls:
  - GlobalTheory.ChF.exists_linDat_of_extSer
  - GlobalTheory.T.exists_linearData_of_split_formalGroup_extension
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Linear data from split extensions

Near a point of bad reduction, the formal group of a degenerating abelian variety is an extension of the formal group $F_B$ of an abelian part by a formal torus $\hat{\mathbb{G}}_m^r$. This section works with such an extension $F$ at the level of formal group laws and tangent spaces. Given a Hodge-Tate datum for the abelian part, together with characters of $F_B$ whose differentials are the Hodge-Tate periods, we produce a *linear datum*: the tangent space $\mathcal{O}^d$ of $F$ as a split extension of $\mathcal{O}^g$ by $\mathcal{O}^r$, with the action of the ring $O_E$, and a finite family of differentials of characters of $F$ that contains the Hodge-Tate periods and a dual basis of the torus part. The colength bounds of the next two sections take a linear datum as input. The theorem is also used directly in the step [every character of the literature](/step/every-character-of-literature/).

Throughout, $C$, $v$ and $\mathcal{O}$ are as in [the first section](/entry/period-datum-main/), and $\mathcal{O}$ is a $\mathbb{Z}_p$-algebra. We use [formal group laws](/learn/formal-groups/#formal-group-laws) and their homomorphisms from the Background. For a $d$-tuple $\varphi$ of power series in $g$ variables without constant term, $\mathrm{lin}(\varphi) \in M_{d \times g}(\mathcal{O})$ is the matrix of linear coefficients, so $\mathrm{lin}$ of a homomorphism is its tangent map. The multiplicative formal group law of dimension $r$ is $\hat{\mathbb{G}}_m^r$, with $(X + Y + XY)_i = X_i + Y_i + X_iY_i$.

### Characters and split extensions

**Definition 4.4.1 (Character of a formal group law).** Let $F$ be a formal group law of dimension $d$ over $\mathcal{O}$. A *character* of $F$ is a power series $u \in \mathcal{O}[[X_1, \dots, X_d]]$ with $u(0) = 1$ and $u(F(X, Y)) = u(X)u(Y)$. Its *differential* is $du = (\partial u/\partial X_j(0))_j \in \mathcal{O}^d$.

So $u - 1$ is a homomorphism from $F$ to $\hat{\mathbb{G}}_m$. For $F = \hat{\mathbb{G}}_m^r$ the series $1 + X_i$ are characters with differentials the unit vectors $e_i$. If $Q : F \to F'$ is a homomorphism and $u$ is a character of $F'$, then $u \circ Q$ is a character of $F$, and the chain rule gives $d(u \circ Q) = \mathrm{lin}(Q)^{\mathsf T}\, du$.

**Definition 4.4.2 (Split exact pair).** Matrices $A \in M_{d \times r}(\mathcal{O})$ and $B \in M_{g \times d}(\mathcal{O})$ form a *split exact pair* if $BA = 0$ and there are $A' \in M_{r \times d}(\mathcal{O})$ and $B' \in M_{d \times g}(\mathcal{O})$ with $A'A = 1$, $BB' = 1$ and $AA' + B'B = 1$.

This says that $0 \to \mathcal{O}^r \xrightarrow{A} \mathcal{O}^d \xrightarrow{B} \mathcal{O}^g \to 0$ is a split short exact sequence.

**Definition 4.4.3 (Extension of formal group laws).** Let $F$ and $F_B$ be formal group laws over $\mathcal{O}$ of dimensions $d$ and $g$. An *extension of $F_B$ by a torus* is a pair of homomorphisms $J : \hat{\mathbb{G}}_m^r \to F$ and $Q : F \to F_B$ such that $(\mathrm{lin}(J), \mathrm{lin}(Q))$ is a split exact pair. The law $F$ has *finite flat $p$-power torsion* if for each $k$ the ring $\mathcal{O}[[X]]/([p^k]_F)$ is a free $\mathcal{O}$-module of finite rank whose elements are separated by the $\mathcal{O}$-algebra maps to $\mathcal{O}$.

The ring $\mathcal{O}[[X]]/([p^k]_F)$ is the coordinate ring of the kernel of $[p^k]$ on $F$. The condition says that $F[p^k]$ is a finite flat group scheme over $\mathcal{O}$ with enough $\mathcal{O}$-points.

### Linear data

Let $O_E$ be a commutative ring with an involution $a \mapsto a^*$, let $O_e = \mathbb{Z}_p \otimes O_E$ with $\sigma = 1 \otimes {}^*$, and let $H$ be a [Hodge-Tate datum](/entry/htd-of-dat/) over $\mathcal{O}$ for $(O_e, \sigma, c_p)$. Write $H_{\cdot i} \in \mathcal{O}^g$ for the column $i$ of its Hodge-Tate matrix, $i \in \mathrm{Ix}$.

**Definition 4.4.4 (Linear datum).** Let $A \in M_{d \times r}(\mathcal{O})$, $B \in M_{g \times d}(\mathcal{O})$, let $\rho_G : O_E \to M_d(\mathcal{O})$ and $N : O_E \to M_r(\mathbb{Z})$ be ring maps, and let $s_1, \dots, s_m \in \mathcal{O}^d$. Then $(H, A, B, \rho_G, N, s)$ is a *linear datum* if:

1. the projectors $P$ and $P_L$ of $H$ are $0$;
2. $(A, B)$ is a split exact pair;
3. $B \rho_G(a) = \rho_L(1 \otimes a) B$ and $\rho_G(a) A = A N(a)$ for all $a \in O_E$;
4. for each $i \in \mathrm{Ix}$ some $s_k$ equals $B^{\mathsf T} H_{\cdot i}$;
5. for each $i \in \{1, \dots, r\}$ some $s_k$ has $A^{\mathsf T} s_k = e_i$.

So $\rho_G$ is the action of $O_E$ on the tangent space of $F$; it acts on the torus part through the integral matrices $N(a)$ and on the abelian part through $\rho_L$. The vectors $s_k$ are covectors on the tangent space of $F$: they contain the Hodge-Tate periods, pulled back from the abelian part, and a dual basis of the torus part.

**Theorem 4.4.5 (Linear data from a split extension).** Let $C$ be an algebraically closed field of characteristic $0$ with a valuation $v$, let $\mathcal{O}$ be the ring of integers of $v$, and assume that $p$ is not a unit in $\mathcal{O}$ and that $\mathcal{O}$ is $p$-adically complete. Let $F$ and $F_B$ be formal group laws over $\mathcal{O}$ of dimensions $d$ and $g$, and let $(J, Q)$ be an extension of $F_B$ by $\hat{\mathbb{G}}_m^r$, where $F$ has finite flat $p$-power torsion. Let $O_E$ be a commutative ring with an involution, let $\rho_G : O_E \to M_d(\mathcal{O})$ and $N : O_E \to M_r(\mathbb{Z})$ be ring maps, and for each $a \in O_E$ let $\alpha_B(a)$ be a $g$-tuple of power series in $g$ variables without constant term. Assume that for all $a$
$$\mathrm{lin}(Q)\, \rho_G(a) = \mathrm{lin}(\alpha_B(a))\, \mathrm{lin}(Q), \qquad \rho_G(a)\, \mathrm{lin}(J) = \mathrm{lin}(J)\, N(a).$$
Assume that there are $c_p \in \mathcal{O}$, a Hodge-Tate datum $H$ for $(\mathbb{Z}_p \otimes O_E, 1 \otimes {}^*, c_p)$ whose conditions of a Hodge-Tate setting hold, and an invertible $S \in M_g(\mathcal{O})$, such that $P = 0$, $P_L = 0$, $\mathrm{lin}(\alpha_B(a))\, S = S\, \rho_L(1 \otimes a)$ for all $a$, and for each $i \in \mathrm{Ix}$ there is a character $u$ of $F_B$ with $S^{\mathsf T} du = H_{\cdot i}$. Then there are $c_p$, a Hodge-Tate datum $H$ in a Hodge-Tate setting, a matrix $B \in M_{g \times d}(\mathcal{O})$ and characters $u_1, \dots, u_m$ of $F$ such that $(H, \mathrm{lin}(J), B, \rho_G, N, (du_k))$ is a linear datum.

Lean: `GlobalTheory.ChF.exists_linDat_of_extSer` (also `GlobalTheory.T.exists_linearData_of_split_formalGroup_extension`, a second name).

*Proof.* Keep $c_p$ and $H$, and put $B = S^{-1}\mathrm{lin}(Q)$. Let $A = \mathrm{lin}(J)$, and let $A'$ and $B'$ be the splittings of the pair $(A, \mathrm{lin}(Q))$. Then $BA = S^{-1}\mathrm{lin}(Q)A = 0$, $A'A = 1$, $B(B'S) = S^{-1}\mathrm{lin}(Q)B'S = 1$, and $AA' + (B'S)B = AA' + B'\mathrm{lin}(Q) = 1$. So $(A, B)$ is a split exact pair. From $\mathrm{lin}(\alpha_B(a))S = S\rho_L(1 \otimes a)$ we get $S^{-1}\mathrm{lin}(\alpha_B(a)) = \rho_L(1 \otimes a)S^{-1}$, so
$$B\rho_G(a) = S^{-1}\mathrm{lin}(\alpha_B(a))\,\mathrm{lin}(Q) = \rho_L(1 \otimes a)\, B.$$
The relation $\rho_G(a)A = AN(a)$ is a hypothesis.

The characters are of two kinds. For $i \in \mathrm{Ix}$, let $u_i'$ be a character of $F_B$ with $S^{\mathsf T} du_i' = H_{\cdot i}$, and take the character $u_i' \circ Q$ of $F$. By the chain rule
$$d(u_i' \circ Q) = \mathrm{lin}(Q)^{\mathsf T} du_i' = \mathrm{lin}(Q)^{\mathsf T} (S^{-1})^{\mathsf T} S^{\mathsf T} du_i' = B^{\mathsf T} H_{\cdot i}.$$
This gives condition 4. For $i \in \{1, \dots, r\}$ we need a character $u_i''$ of $F$ with $A^{\mathsf T} du_i'' = e_i$. This is the lifting lemma of the remark below: since $F$ has finite flat $p$-power torsion and $\mathrm{lin}(J)$ has the left inverse $A'$, it gives a character $u_i''$ of $F$ with $A^{\mathsf T} du_i'' = e_i$. This gives condition 5, and the family $(u_k)$ is the union of the $u_i' \circ Q$ and the $u_i''$, indexed by $\mathrm{Ix}$ and $\{1, \dots, r\}$, so $m = 2g + r$. $\square$

**Remark 4.4.6.** The lifting of torus characters is a separate lemma: if $F$ has finite flat $p$-power torsion, $J : \hat{\mathbb{G}}_m^r \to F$ is a homomorphism and $A'\,\mathrm{lin}(J) = 1$, then for each $i$ there is a character $u$ of $F$ with $\mathrm{lin}(J)^{\mathsf T} du = e_i$. Only this lemma uses the torsion of $F$; the rest of the proof is linear algebra.

**Remark 4.4.7 (Formalization).** The series $\alpha_B(a)$ need not be endomorphisms of $F_B$: only their linear parts enter the statement. The second name is proved by `first | exact @GlobalTheory.ChF.exists_linDat_of_extSer | ...` at [ExistsLinearDataOfSplitFormalGroupExtensionStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/ExistsLinearDataOfSplitFormalGroupExtensionStatement.lean#L21), with a raised heartbeat limit at line 19. The conclusion returns the same $c_p$ and $H$ as the hypothesis.
