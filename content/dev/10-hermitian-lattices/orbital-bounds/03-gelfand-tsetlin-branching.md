---
title: Gelfand-Tsetlin branching for the dual Weyl modules
decls:
  - gelfand_tsetlin_branching
  - gTLower_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Gelfand-Tsetlin branching for the dual Weyl modules

This section proves the branching law of Gelfand and Tsetlin for the restriction from $\mathrm{GL}_N(\mathbb{C})$ to $\mathrm{GL}_{N-1}(\mathbb{C})$, in the model of the dual Weyl modules inside a polynomial ring. Each irreducible representation of $\mathrm{GL}_{N-1}$ that occurs has multiplicity one, and it occurs exactly when its highest weight interlaces the highest weight of the representation of $\mathrm{GL}_N$. With the branching law in hand, the section then proves the existence of integral and bounded branching maps from the integral duality of Weyl modules. The branching maps are used to [build the pairs of the interlacing branching](/entry/branching-interlacing-pairs/). The background is in [representations of a group](/learn/representations/#representations-of-a-group) and [highest weights and branching](/learn/representations/#highest-weights-and-branching).

### The dual Weyl modules

We use the notation of the section on [branching maps between Weyl modules](/entry/wgl-g-tlower-of/). For a dominant weight $\lambda$ of length $N$, $\nabla_R(\lambda) \subseteq R[X]$ is the dual Weyl module in the polynomial ring of the $N \times N$ matrix $X = (x_{ij})$, $\Delta_R(\lambda)$ is the Weyl module, $e_\lambda$ is the extremal vector, and $\langle \cdot, \cdot \rangle_\lambda$ is the normalized Fock pairing. The group $\mathrm{GL}_N(R)$ acts on $R[X]$ by $(g \cdot f)(X) = \det(g)^{d(\lambda)} f(g^{\mathsf T} X)$.

Let $n + 1 = N$. Embed $\mathrm{GL}_n$ into $\mathrm{GL}_N$ by $g \mapsto \mathrm{diag}(g, 1)$. A dominant weight $\mu$ of length $n$ *interlaces* $\lambda$ if
$$\lambda_{i+1} \leq \mu_i \leq \lambda_i \quad \text{for all } i < n.$$

**Definition 4.3.1 (Equivariant branching map).** Let $\mu$ be dominant of length $n$. A $\mathbb{C}$-linear map $\varphi : \mathbb{C}[X_n] \to \mathbb{C}[X_N]$ is an *equivariant branching map* from $\mu$ to $\lambda$ if $\varphi$ maps $\nabla_{\mathbb{C}}(\mu)$ into $\nabla_{\mathbb{C}}(\lambda)$ and
$$\varphi(g \cdot s) = \mathrm{diag}(g, 1) \cdot \varphi(s) \quad \text{for all } g \in \mathrm{GL}_n(\mathbb{C}),\ s \in \nabla_{\mathbb{C}}(\mu).$$

### The branching law

**Theorem 4.3.2 (Gelfand-Tsetlin branching).** Let $n + 1 = N$ and let $\lambda$ be dominant of length $N$.

1. Let $\mu$ be dominant of length $n$, and let $\varphi$ and $\varphi'$ be equivariant branching maps from $\mu$ to $\lambda$. If $\varphi'(s) \neq 0$ for some $s \in \nabla_{\mathbb{C}}(\mu)$, then $\mu$ interlaces $\lambda$, and there is $c \in \mathbb{C}$ with $\varphi(s) = c\, \varphi'(s)$ for all $s \in \nabla_{\mathbb{C}}(\mu)$.
2. $\nabla_{\mathbb{C}}(\lambda)$ is the sum of the subspaces $\varphi(\nabla_{\mathbb{C}}(\mu))$, over all dominant $\mu$ of length $n$ that interlace $\lambda$ and all equivariant branching maps $\varphi$ from $\mu$ to $\lambda$.

Lean: `gelfand_tsetlin_branching`.

Part 1 says that the multiplicity of $\nabla_{\mathbb{C}}(\mu)$ in the restriction is at most one, and is zero unless $\mu$ interlaces $\lambda$. Part 2 says that the interlacing pieces fill the space.

*Proof.* This is an assembly lemma applied to the theorem on highest weights and to five proved steps. The theorem on highest weights says that $\nabla_{\mathbb{C}}(\lambda) = \Delta_{\mathbb{C}}(\lambda)$, that $\nabla_{\mathbb{C}}(\lambda)$ is irreducible, and that the vectors of $\nabla_{\mathbb{C}}(\lambda)$ fixed by the upper unitriangular matrices are the multiples of $e_\lambda$. Call a vector *$n$-extremal of weight $\mu$* if it is fixed by the upper unitriangular matrices of $\mathrm{GL}_n$, embedded in $\mathrm{GL}_N$, and the diagonal torus of $\mathrm{GL}_n$ acts on it by the character $\mu$. The five steps are these.

1. *Extremal facts.* The vector $e_\mu$ is fixed by the upper unitriangular group of $\mathrm{GL}_n$, it has torus weight $\mu$, and $\nabla_{\mathbb{C}}(\mu)$ is stable under $\mathrm{GL}_n$. This step is derived from the theorem on highest weights.
2. *Fixed line.* Two $n$-extremal vectors of $\nabla_{\mathbb{C}}(\lambda)$ of the same weight $\mu$ are proportional, and $\mu$ interlaces $\lambda$.
3. *Stable complements.* Every $\mathrm{GL}_n$-stable subspace $W \subseteq \nabla_{\mathbb{C}}(\lambda)$ has a $\mathrm{GL}_n$-stable complement.
4. *Highest vectors.* Every nonzero $\mathrm{GL}_n$-stable subspace $W \subseteq \nabla_{\mathbb{C}}(\lambda)$ contains a nonzero $n$-extremal vector of some weight $\mu$.
5. *Realization.* Every $n$-extremal vector $f \in \nabla_{\mathbb{C}}(\lambda)$ of weight $\mu$ is $\varphi(e_\mu)$ for an equivariant branching map $\varphi$ from $\mu$ to $\lambda$. This step is derived from the theorem on highest weights and steps 1 to 4.

For part 1, the image $\varphi'(\nabla_{\mathbb{C}}(\mu))$ is a nonzero quotient of the irreducible module $\nabla_{\mathbb{C}}(\mu)$, so $\varphi'$ is injective on it. The images $\varphi(e_\mu)$ and $\varphi'(e_\mu)$ are $n$-extremal of weight $\mu$ by step 1. Step 2 makes them proportional and gives the interlacing. Two equivariant maps that agree on $e_\mu$ agree on the module it generates, which is $\nabla_{\mathbb{C}}(\mu)$. For part 2, let $W$ be the sum of the images. It is stable. Step 3 gives a stable complement $W'$. If $W' \neq 0$, step 4 gives an $n$-extremal vector in $W'$ of some weight $\mu$, which interlaces $\lambda$ by step 2. Step 5 puts this vector in the image of a branching map, hence in $W$. This contradicts $W \cap W' = 0$. So $W' = 0$ and $W = \nabla_{\mathbb{C}}(\lambda)$. $\square$

The argument in the proof is the one the assembly lemma carries out, read off from the statements of the steps; the steps themselves were not unfolded.

### Integral branching maps

**Theorem 4.3.3 (Gelfand-Tsetlin lowering from integral duality).** Assume the integral duality of Weyl modules: for every dominant $\lambda$ and every $f \in \nabla_{\mathbb{Q}}(\lambda)$, the pairing $\langle f, g \rangle_\lambda$ is an integer for all $g \in \nabla_{\mathbb{Z}}(\lambda)$ if and only if $f$ is the image of an element of $\Delta_{\mathbb{Z}}(\lambda)$. Then for every $n + 1 = N$, every dominant $\lambda$ of length $N$ and every dominant $\sigma$ of length $n$ that interlaces $\lambda$, the conclusion of the theorem on [Gelfand-Tsetlin lowering](/entry/wgl-g-tlower-of/) holds. That is, $c(\lambda, \sigma) \neq 0$, $|c(\lambda, \sigma)| \leq C$, $\xi \neq 0$ and $\deg = \lambda_0 - D_0$, and there are linear maps $\iota : \mathbb{C}[X_n] \to \mathbb{C}[X_N]$ and $\beta : \mathbb{C}[X_N] \to \mathbb{C}[X_n]$ with these properties.

1. $\iota$ is an equivariant branching map from $\sigma$ to $\lambda$ that maps $\nabla_{\mathbb{Z}}(\sigma)$ into $\nabla_{\mathbb{Z}}(\lambda)$, on whose image the last diagonal torus $t(a)$ acts by $a^{\deg}$, with $\iota(e_\sigma) = c(\lambda, \sigma)\, \xi$ and $\operatorname{Re} \langle \iota s, \iota s \rangle_\lambda \leq B^2 \operatorname{Re} \langle s, s \rangle_\sigma$.
2. $\beta$ maps $\Delta_{\mathbb{C}}(\lambda)$ into $\Delta_{\mathbb{C}}(\sigma)$ and $\Delta_{\mathbb{Z}}(\lambda)$ into $\Delta_{\mathbb{Z}}(\sigma)$, it is not zero on $\Delta_{\mathbb{C}}(\lambda)$, it satisfies $\beta(\mathrm{diag}(g, 1) \cdot f) = g \cdot \beta(f)$ and $\beta(t(a) \cdot f) = a^{\deg} \beta(f)$, and $\operatorname{Re} \langle \beta f, \beta f \rangle_\sigma \leq B^2 \operatorname{Re} \langle f, f \rangle_\lambda$.
3. $\langle \iota s, f \rangle_\lambda = \langle s, \beta f \rangle_\sigma$ for $s \in \nabla_{\mathbb{C}}(\sigma)$ and $f \in \Delta_{\mathbb{C}}(\lambda)$.

Here $c(\lambda, \sigma)$, $C$, $B$, $\xi$, $D_0$ and $\deg$ are the branching data defined in that section.

Lean: `gTLower_of`.

*Proof.* This is [Gelfand-Tsetlin lowering](/entry/wgl-g-tlower-of/) applied to four inputs. The first is the integral duality, which is the hypothesis. The second is the theorem on highest weights, quoted in the proof above. The third is the Gelfand-Tsetlin branching theorem above. The fourth is the Schur bound: if $s \in \nabla_{\mathbb{C}}(\lambda)$ and $|s(x)| \leq 1$ for all $x \in U(N)$, then $\langle s, s \rangle_\lambda \leq \dim \Delta_{\mathbb{C}}(\lambda)$. $\square$

**Example 4.3.4.** Take $N = 2$, $n = 1$ and $\lambda = (\lambda_0, \lambda_1)$. The weights of length $1$ that interlace $\lambda$ are the integers $\mu_0$ with $\lambda_1 \leq \mu_0 \leq \lambda_0$. There are $\lambda_0 - \lambda_1 + 1$ of them, and each piece $\nabla_{\mathbb{C}}(\mu_0)$ is a line. So part 2 of the branching law gives $\dim \nabla_{\mathbb{C}}(\lambda) \leq \lambda_0 - \lambda_1 + 1$, and part 1 shows that the pieces are distinct, as the torus $\mathrm{GL}_1$ acts on them by distinct characters. This is the dimension of the representation of $\mathrm{GL}_2$ of highest weight $\lambda$.

**Remark 4.3.5 (Formalization).** The theorem on lowering from integral duality has the same short name as the theorem on [Gelfand-Tsetlin lowering](/entry/wgl-g-tlower-of/) that it calls, in a different namespace; see [GTLower.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/GTLower.lean#L7). The integral duality is a hypothesis; its caller supplies it. The branching law is stated for linear maps on the whole polynomial ring, with the conditions only on $\nabla_{\mathbb{C}}(\mu)$. The assembly lemma and the five steps were not unfolded beyond their statements; the assembly lemma is in [ConstructionD.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/GelfandTsetlinBranching/ConstructionD.lean#L139). The branching law is in [GTBranch.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/GTBranch.lean#L4).
